from flask import Flask, jsonify
from .config import app_config
from .models import db

def create_app(env_name):
  """
  Create app
  """

  # app initialization
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  db.init_app(app)

  from src.api import bp as api_bp
src.register_blueprint(api_bp, url_prefix='/api')

  @app.route('/', methods=['GET'])
  def index():
    return 'Congratulations! Your first endpoint is actually working!'

  @app.route('/ingredients', methods=['GET'])
  def get_all_inredients():
    return RawDataModel.query.all()

  @app.route('/hello/<string:username>')
  def say_hello(username):
    return 'Hello, %s'%username


  return app