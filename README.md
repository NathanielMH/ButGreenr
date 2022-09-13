# ButGreenr
Code for the app developed for the Recircula challenge 2022.
This app is designed to initiate a movement and allow for food waste reduction in the household scale. It is one I have presented in the Recircula challenge final with my team.
This folder includes the design of a search algorithm for recipe recommendation given a set of ingredients with their respective quantities based on the give data set from Recipe_DB.
The implementation of the recommendation includes a priority queue using heaps, that allows an for an efficient search. 
It also allows the possibility to get a recommendation with a Deep Neural Network implemented in Tensorflow with the Keras API. (In progress)
Try it out for yourself!

## How it works
As a working example of the app, it accept ingredients of the following format:
[INGREDIENT1] : [AMOUNT_IN_GRAMS]; [INGREDIENT2] : [AMOUNT_IN_GRAMS]; ...
where every ingredient name matches exactly the name of its representative in the database.
