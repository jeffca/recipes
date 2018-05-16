from recipes import app, get_db
from flask import Flask, render_template, request, redirect, url_for, flash, Response, jsonify
from recipes.models import Recipe
# from stretching.database import db_session
# import datetime 	
# from datetime import timedelta
# from flask_mail import Message
# from sqlalchemy import desc
# from functools import wraps

# Recipe.create_table(fail_silently=True)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/recipes')
def recipes():
	allRecipes = []
	for recipe in Recipe.select():
		allRecipes.append({
			'recipe': recipe.recipe,
			'ingredients': recipe.ingredients,
			'instructions': recipe.instructions,
			'menuimgurl': recipe.menuimgurl,
			'category': recipe.category
		})
	return jsonify(allRecipes)
