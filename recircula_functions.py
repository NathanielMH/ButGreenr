import json
from typing import List, Union, Dict
from pq_vec import Priority_queue as pq

# from recipes import User_recipe

path = "recipes.json"
with open(path) as file:
    recipes = json.load(file)

path = "ingredients.json"
with open(path) as file:
    ingredients = json.load(file)


def missing_ingredients(my_recipe, recipe) -> List:
    missing_ingr = []
    for i in range(len(my_recipe)):
        dif = recipe[i] - my_recipe[i]
        if dif > 0:
            missing_ingr.append(dif)
        else:
            missing_ingr.append(0)
    return missing_ingr


def diff_score(v1: List, v2: List) -> float:
    s = 0
    t = 0
    for i in range(len(v1) - 3):
        if v1[i] == 0 and v2[i] != 0:
            t += 1
        if v1[i] < v2[i]:
            s += (float(v1[i]) - float(v2[i])) ** 2
    return s  # formula in terms of s and t


def k_closest_recipes(my_ingredients: List[float], recipes: List[Dict[str, Union[str, List, float]]],
                      k: int) -> List[Dict[str, Union[str, List, float]]]:
    for i in range(len(recipes)):
        recipes[i]["score"] = diff_score(recipes[i]["ingredient_list"], my_ingredients)
    Q = pq(recipes)
    closest_k = []
    for i in range(k):
        closest_k.append(Q.remove_min())
    return closest_k


def scale_recipes(recipes: List[Dict[str, Union[str, List, float]]], serving: float) -> None:
    for i in range(len(recipes)):
        for j in range(len(recipes[0]["ingredient_list"])):
            if recipes[i]["total_weight"] != 0:
                recipes[i]["ingredient_list"][j] *= serving / recipes[i]["total_weight"]


def exec(my_ingredients:List, recipes: List[Dict[str, Union[str, List, float]]],serving:float, k=5) -> List[Dict[str, Union[str, List, float]]]:
    scale_recipes(recipes, serving)
    closest_k = k_closest_recipes(my_ingredients, recipes, k)
    for j in range(k):
        closest_k[j]["missing_ingredients"] = missing_ingredients(my_ingredients, closest_k[j]["ingredient_list"])
    return closest_k


def recipe_builder(ingredients_string: str, ingredients:List):
    my_ingredients = []
    l = ingredients_string.split(";")
    ingr_list = []
    amount = {}
    for ingredient in l:
        name_amount = ingredient.split(":")
        ingr_list.append(name_amount[0])
        amount[name_amount[0]] = float(name_amount[1])
    for i in range(len(ingredients)):
        if ingredients[i] in ingr_list:
            my_ingredients.append(amount[ingredients[i]])
        else:
            my_ingredients.append(0)
    return my_ingredients


my_ingredients = []
for i in range(len(ingredients)):
    if ingredients[i] in ['apples, raw, with skin', 'vanilla extract', 'yogurt, greek, plain, nonfat']:
        my_ingredients.append(250)
    else:
        my_ingredients.append(0)

answer = exec(my_ingredients, recipes, 100)
