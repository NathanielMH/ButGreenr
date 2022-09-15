import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from recircula_functions import exec, recipe_builder
from recircula_functions import recipes, ingredients
import tensorflow as tf
import numpy as np


class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text='Ingredients:'))
        self.recipe = TextInput()
        self.add_widget(self.recipe)

        self.add_widget(Label(text='Serving size:'))
        self.serving_size = TextInput()
        self.add_widget(self.serving_size)

        self.press = Button(text='Recommend')
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)

        self.answer = Label(text="")
        self.add_widget(self.answer)

    def click_me(self, instance):
        # normalize recipe
        my_ingredients = recipe_builder(self.recipe.text, ingredients)
        # answer = exec(my_ingredients, recipes, float(self.serving_size.text))
        model = tf.keras.models.load_model('recipe_model.h5')
        my_input = np.array([my_ingredients])
        model_ans = model.predict(my_input)
        answer_class = np.argmax(model_ans)
        answer = recipes[answer_class]
        self.answer.text += answer["name"] + "\n"


class parentApp(App):
    def build(self):
        return childApp()


if __name__ == "__main__":
    parentApp().run()
