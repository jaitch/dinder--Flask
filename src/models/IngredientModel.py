from marshmallow import fields, Schema
import datetime
from . import db

class Ingredient(db.Model):
  """
  Ingredient Model
  """

  # table name
  __tablename__ = 'ingredients'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    self.name = data
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  @staticmethod
  def get_all_ingredientss():
    return IngredientModel.query.all()

  @staticmethod
  def get_one_ingredient(id):
    return IngredientModel.query.get(id)

  def __repr(self):
    return '<id {}>'.format(self.id)

  def __repr(self):
    return '<id {}>'.format(self.id)