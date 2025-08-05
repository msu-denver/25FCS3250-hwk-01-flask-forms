'''
CS3250 - Software Development Methods and Tools - Fall 2025
Instructor: Thyago Mota
Student:
Description: Homework 01 - Forms for the Recipes Web App
'''

from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateField, SelectField, SubmitField, validators
from wtforms.validators import DataRequired

# TODO #2: complete the recipe form with the missing fields (title, type, and tags)
class RecipeForm(FlaskForm):
    number = StringField('Recipe#', validators=[DataRequired()])
    submit = SubmitField('Submit')