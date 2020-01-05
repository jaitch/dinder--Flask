from flask import Flask, abort
from .config import app_config
from .models import db

def create_app(env_name):
  """
  Create app
  """

  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  db.init_app(app)

  from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return 'Congratulations! Your first endpoint is actually working!'

  @app.route('/hello/<string:username>')
  def say_hello(username):
    return 'Hello, %s'%username


  return app