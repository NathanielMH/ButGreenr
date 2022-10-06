import tensorflow as tf
from recircula_functions import recipes
import numpy as np
import random
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pickle

NUM_AUGMENT = 10000
MAX_RECIPES = 10000
epsilon = 1e-10

file = open('recipe_data_x', 'rb')
X = pickle.load(file)
file.close()

file = open('recipe_data_y', 'rb')
y = pickle.load(file)
file.close()

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y)

num_recipes = MAX_RECIPES

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
    X_train,
    y_train,
    epochs=300
)

loss, accuracy = model.evaluate(X_test, y_test)

# Make predictions
preds = model.predict(X_test)

# Plot model predictions
plt.figure(figsize=(12, 12))

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
    plt.xlabel('i={} | pred={} | true={}'.format(start_index + i, pred, actual), color=col)
plt.show()
model.save('recipe_model.h5')
