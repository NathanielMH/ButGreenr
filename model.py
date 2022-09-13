import tensorflow as tf
from recircula_functions import recipes
import numpy as np
import random
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

NUM_AUGMENT = 0
epsilon = 1e-10

# Make the recipes treatable by a NN
X = []
y = []
for i in range(len(recipes)):
    X.append(recipes[i]["ingredient_list"])
    one_hot = np.zeros(len(recipes))
    one_hot[i] = 1
    y.append(one_hot)
# Augment data to have proper amounts, and be able to test too.
for k in range(NUM_AUGMENT):
    for i in range(len(X)):
        noise = 10
        augmented = X[i]
        augmented_list = []
        label_augmented = []
        for j in range(len(X[i])):
            n = random.randint(0, 1)
            if n % 2 == 0:
                augmented[j] += noise
                augmented_list.append(augmented)
                label_augmented.append(y[i])
                k = random.randint(0, 1)
                if k % 2 == 2:
                    augmented[j] -= noise

    X += augmented_list
    y += label_augmented

X = np.array(X)
y = np.array(y)

# Normalize the data

X_mean = np.mean(X)
X_std = np.std(X)

X_norm = (X - X_mean) / (X_std + epsilon)

X_train_norm, X_test_norm, y_train, y_test = train_test_split(X_norm,y)

num_recipes = len(recipes)

# Due to the nature of the model we are training, we will use no test set.

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(num_recipes, activation="softmax")
])

model.compile(
    optimizer='sgd',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
h = model.fit(
    X_train_norm,
    y_train,
    epochs=300
)

loss, accuracy = model.evaluate(X_test_norm, y_test)

# Make predictions
preds = model.predict(X_test_norm)

# Plot model predictions
plt.figure(figsize = (12, 12))

start_index = 0

for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    pred = np.argmax(preds[start_index + i])
    actual = np.argmax(y_test[start_index + i])
    col = 'g'
    if pred != actual:
        col = 'r'
    plt.xlabel('i={} | pred={} | true={}'.format(start_index + i, pred, actual), color = col)
plt.show()
model.save('recipe_model.h5')
