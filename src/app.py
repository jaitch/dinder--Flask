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
    return 'Congratulations! Your first endpoint is actually working!'

  @app.route('/ingredients', methods=['GET'])
  @cross_origin(supports_credentials=True)
  def get_all_ingredients():
    ingredients_schema = IngredientSchema(many=True)
    return jsonify(ingredients_schema.dump(Ingredient.query.limit(10).all()))

  @app.route('/ingredient/<sought_ingredient>', methods=['GET'])
  @cross_origin(supports_credentials=True)
  def get_ingredient_by_name(sought_ingredient):
    ingredient_schema = IngredientSchema(many=True)
    found_ingredient = Ingredient.query.filter_by(name=sought_ingredient)
    if found_ingredient is None:
      response = {
        'message': 'Sorry. Ingredient does not exist.'
      }
      return jsonify(response), 404
    result = ingredient_schema.dump(found_ingredient)
    result_call = result[0]["name"]
    sql = text(f"select i.id, i.name, t.id, t.name, s.strength from ingredients i, similarities s, ingredients t  where t.id=s.target and i.id=s.source and i.name='{result_call}' order by s.strength desc")
    sims = db.engine.execute(sql)
    print(sims)
    # response= {
    #   'data': sims,
    #   'status_code' : 200
    # }
    # d, a = {}, []
    # for rowproxy in sims:
    # # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
    #   for column, value in rowproxy.items():
    #     # build up the dictionary
    #     d = {**d, **{column: value}}
    #   a.append(d)
    # sim_results = json.dumps[{column: value for column, value in rowproxy.items()} for rowproxy in sims]
    sim_results = json.dumps({'response': [dict(row) for row in sims]})
    print('this is the json', sim_results)
    return sim_results

    # future reference: use intersect or intersect_all or union in queries to do multiple ingredient searches. use 'values' to measure which has the most recipes? or return all possible and let the user choose?

  @app.route('/recipes', methods=['GET'])
  @cross_origin(supports_credentials=True)
  def get_all_recipes():
    schema = RawDataSchema(many=True)
    return jsonify(schema.dump(RawDataModel.query.limit(10).all()))

  @app.route('/recipe/<id>', methods=['GET'])
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

    if __name__ == "__main__":
      app.run(host='0.0.0.0', port=8000, debug=True)

  return app