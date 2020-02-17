from flask import Flask, jsonify, request, abort, send_from_directory
from flask_cors import CORS, cross_origin
from sqlalchemy import text
from src.models.RawDataModel import RawDataModel, RawDataSchema
from src.models.IngredientModel import Ingredient, IngredientSchema
from .config import app_config
from .models import db
import json


def create_app(env_name):
  app = Flask(__name__, static_url_path='')
  CORS(app, support_credentials=True)
  app.config.from_object(app_config[env_name])
  db.init_app(app)

  @app.route('/', methods=['GET'])
  def index():
    return 'This index endpoint is working!'

  @app.route('/ingredients')
  @cross_origin(supports_credentials=True)
  def get_all_ingredients():
    ingredients_schema = IngredientSchema(many=True)
    return jsonify(ingredients_schema.dump(Ingredient.query.limit(10).all()))

  @app.route('/ingredient/<sought_ingredient>/<y>')
  @cross_origin(supports_credentials=True)
  def get_ingredient_by_name(sought_ingredient, y):
    ingredient_schema = IngredientSchema(many=True)
    found_ingredient = Ingredient.query.filter_by(name=sought_ingredient)
    if found_ingredient is None:
      response = {
        'message': 'Sorry. Ingredient does not exist.'
      }
      return jsonify(response), 404
    result = ingredient_schema.dump(found_ingredient)
    result_call = result[0]["name"]
    sql = text(f"select i.id as source_id, i.name as source_name, t.id as target_id, t.name as target, s.strength from ingredients i, similarities s, ingredients t  where t.id=s.target and i.id=s.source and i.name='{result_call}' and s.strength>{y} and i.id!=t.id order by s.strength desc")
    sims = db.engine.execute(sql)
    print(sims)
    sim_results = jsonify({'ing_data': [dict(row) for row in sims]})
    print('this is the ing json', sim_results)
    return sim_results

  @app.route('/recipes/')
  @cross_origin(supports_credentials=True)
  def get_matching_recipes():
    schema = RawDataSchema(many=True)
    array = request.args.getlist("ing")
    num = len(array)
    string = ', '.join(str(e) for e in array)
    sql = text(f"select r.* from (select max(recipe_id), count(recipe_id) from ingredients i, recipe_ingredients ri  where i.id=ri.ingredient_id and i.id in ({string} ) group by recipe_id having count(recipe_id)={num}) as foo, raw_data r where foo.max=r.id;")
    recipes = db.engine.execute(sql)
    if recipes is None:
      return []
    print(recipes)
    recipes_to_send = jsonify({'rec_data': [dict(row) for row in recipes]})
    print('this is the rec json', recipes_to_send)
    return recipes_to_send
    # return jsonify(schema.dump())

  @app.route('/recipe/<id>')
  @cross_origin(supports_credentials=True)
  def get_recipe_by_id(id):
    schema = RawDataSchema(many=False)
    # recipe = RawDataModel.query.get(id)
    # print(recipe.allData)
    return jsonify(schema.dump(RawDataModel.query.get(id)))

  @app.route('/json/<path:path>')
  @cross_origin(supports_credentials=True)
  def get_json(path):
    return send_from_directory('data', path)

    # if __name__ == "__main__":
    #   app.run(host='0.0.0.0', port=8000, debug=True)

  return app