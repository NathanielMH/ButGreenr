import json
from typing import List, Dict
from recipes import Factor_recipe

path = "recipes_with_nutritional_info.json"

with open(path) as file:
    data = json.load(file)

# quantity = int(input("How many grams of food do you want to eat?"))

ingredients = []

for i in range(len(data)):
    for j in range(len(data[i]['ingredients'])):
        if data[i]['ingredients'][j]['text'] not in ingredients:
            ingredients.append(data[i]['ingredients'][j]['text'])

ingredients.sort()

save_path = "ingredients.json"
with open(save_path, 'w') as file:
    json.dump(ingredients, file)

recipes = []

for i in range(len(data)):
    recipe_ingr = []
    ingr_list = []
    for k in range(len(data[i]['ingredients'])):
        recipe_ingr.append(data[i]['ingredients'][k]['text'])
    l = 0
    for j in range(len(ingredients)):
        total_weight = 0
        if ingredients[j] in recipe_ingr:
            ingr_list.append(data[i]['weight_per_ingr'][l])
            total_weight += data[i]['weight_per_ingr'][l]
            l += 1
        else:
            ingr_list.append(0)
    recipes.append({"ingredient_list": ingr_list, "name": data[i]['title'], "score": 0., "total_weight": total_weight})

save_path = "recipes.json"
with open(save_path, 'w', encoding='utf-8') as file:
    print("Generating json...")
    json.dump(recipes, file, ensure_ascii=False, indent=4)
