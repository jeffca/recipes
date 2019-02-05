from recipes import app
from flask import Flask, render_template, request, redirect, url_for, flash, Response, jsonify
from recipes.models import *
# from stretching.database import db_session
# import datetime 	
# from datetime import timedelta
# from flask_mail import Message
# from sqlalchemy import desc
# from functools import wraps

# Recipe.create_table(fail_silently=True)

@app.route('/')
def home():
	recipes = Recipe.select()
	categories = Category.select().order_by(Category.order)
	return render_template('index.html', categories=categories)

@app.route("/newCategoryMapping", methods=['GET', 'POST'])
def newCategoryMapping():
	if request.method == 'POST':
		print(request.form.getlist('category'))
		for c in request.form.getlist('category'):
			Recipe_Category.create(recipe_id = request.form.get('recipe'), 
				category_id = c)
		return home()
	else:
		recipes = Recipe.select()
		categories = Category.select().order_by(Category.order)
		return render_template("newCategoryMapping.html", recipes=recipes, categories=categories)

@app.route("/newRecipe", methods=["GET", "POST"])
def newRecipe():
	if request.method == 'GET':
		return render_template("newRecipe.html")
	else:
		Recipe.create(recipe=request.form.get('name'), 
			ingredients=request.form.get('ingredients'), 
			instructions=request.form.get('instructions'), 
			menuimgurl=request.form.get('imageurl'))
		return home()

@app.route("/category/<category_id>")
def categorydetail(category_id):
	recipes = Recipe.select().join(Recipe_Category).join(Category).where(Recipe_Category.category_id == category_id)
	category = Category.select().where(Category.id == category_id).first()
	return render_template("category.html", recipes=recipes, category=category)

@app.route("/category/<category_id>/recipe/<recipe_id>")
def detail(category_id, recipe_id):
	recipe = Recipe.select().where(Recipe.id == recipe_id).first()
	category = Category.select().where(Category.id == category_id).first()
	return render_template('recipe.html', recipe=recipe, category=category)


@app.route('/recipes')
def recipes():
	allRecipes = []
	for recipe in Recipe.select():
		allRecipes.append({
			'id': recipe.id,
			'recipe': recipe.recipe,
			'ingredients': recipe.ingredients,
			'instructions': recipe.instructions,
			'menuimgurl': recipe.menuimgurl,
		})
	return jsonify(allRecipes)
