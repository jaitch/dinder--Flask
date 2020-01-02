from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .RawDataModel import RawDataModel#, RawDataSchema
from .IngredientModel import IngredientModel
