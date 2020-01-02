from marshmallow import fields, Schema
import datetime
from . import db

class IngredientModel(db.Model):
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

  def __repr(self):
    return '<id {}>'.format(self.id)