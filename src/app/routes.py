'''
CS3250 - Software Development Methods and Tools - Fall 2025
Instructor: Thyago Mota
Student:
Description: Homework 01 - Routes for the Recipes Web App
'''

from app import app
from flask import render_template, redirect, url_for, request
from app.forms import RecipeForm

recipes = [
    {'number': 1, 'title': 'Feijoada', 'type': 'main course', 'tags': 'brazilian, rich, ethnical'}, 
    {'number': 2, 'title': 'Pudim de Leite', 'type': 'dessert', 'tags': 'brazilian, easy'}, 
    {'number': 3, 'title': 'Meatloaf', 'type': 'main course', 'tags': 'easy'}
]

@app.route('/')
@app.route('/recipes')
@app.route('/index.html')
def list_recipes():
    return render_template("index.html", recipes=recipes)

@app.route('/recipes/create', methods=['GET','POST'])
def create_recipe():
    form = RecipeForm()
    if form.validate_on_submit(): 
        # TODO #3: complete the append line with the missing fields
        
        return redirect(url_for('list_recipes'))
    else:
       return render_template('recipes_create.html', form=form)
    