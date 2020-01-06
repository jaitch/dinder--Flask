from flask import Blueprint

bp = Blueprint('api', __name__)

from src.api import ingredients, recipes, errors