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

# Make the recipes treatable by a NN
X = []
y = []

for i in range(MAX_RECIPES):
    X.append(recipes[i]["ingredient_list"])
    one_hot = np.zeros(MAX_RECIPES)
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

# if it does not exist, create, else load.

file_x = open('recipe_data_x', 'wb')
pickle.dump(X, file_x)
file_x.close()
file_y = open('recipe_data_y', 'wb')
pickle.dump(y, file_y)
file_y.close()
