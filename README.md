# ButGreenr
Code for the app developed for the Recircula challenge 2022.
This app is designed to initiate a movement and allow for food waste reduction in the household scale. It is one I have presented in the Recircula challenge final with my team.
This folder includes the design of a search algorithm for recipe recommendation given a set of ingredients with their respective quantities based on the give data set from Recipe_DB.
The implementation of the recommendation includes a priority queue using heaps, that allows an for an efficient search. 
It also allows the possibility to get a recommendation with a Deep Neural Network implemented in Tensorflow with the Keras API.
Try it out for yourself!

## How it works
As a working example of the app, it accept ingredients of the following format:
[INGREDIENT1] : [AMOUNT_IN_GRAMS]; [INGREDIENT2] : [AMOUNT_IN_GRAMS]; ...
where every ingredient name matches exactly the name of its representative in the database.

## Neural Network
It is a simple sequential model with two fully connected (Dense) layers with 64 and 16 nodes respectively, and an output layer with a softmax activation to give predictions about recipes. In order to obtain more data, I performed data augmentation by taking a recipe and adding some noise to it, with certain probabilities so as to randomly modify the recipe by a small amount, as well as changin serving sizes, and keeping the same label. The data for now has 1000 recipes and +3500 engineered examples by recipe, and it has been pickled to be able to tune the model without having to create them every time. 

