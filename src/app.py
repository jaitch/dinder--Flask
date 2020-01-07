from flask import Flask, jsonify, request, abort
from src.models.RawDataModel import RawDataModel, RawDataSchema
from src.models.IngredientModel import Ingredient, IngredientSchema
from .config import app_config
from .models import db

def create_app(env_name):
  app = Flask(__name__)
  app.config.from_object(app_config[env_name])
  db.init_app(app)

  @app.route('/', methods=['GET'])
  def index():
    return 'Congratulations! Your first endpoint is actually working!'

  @app.route('/ingredients', methods=['GET'])
  def get_all_ingredients():
    ingredients_schema = IngredientSchema(many=True)
    return jsonify(ingredients_schema.dump(Ingredient.query.limit(10).all()))

  @app.route('/ingredient/<id>', methods=['GET'])
  def get_ingredient_by_id(id):
    ingredient_schema = IngredientSchema(many=False)
    ingredient=Ingredient.query.get(id)
    return jsonify(ingredient_schema.dump(ingredient.name))

  @app.route('/recipes', methods=['GET'])
  def get_all_recipes():
    schema = RawDataSchema(many=True)
    return jsonify(schema.dump(RawDataModel.query.limit(10).all()))

  @app.route('/recipe/<id>', methods=['GET'])
  def get_recipe_by_id(id):
    schema = RawDataSchema(many=False)
    recipe = RawDataModel.query.get(id)
    print(recipe.allData)
    return jsonify(schema.dump(recipe.allData))

  return app