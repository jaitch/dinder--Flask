from flask import Flask, jsonify
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

  # @staticmethod
  # def get_all_ingredients():
  #   return jsonify(Ingredient.query.all())

  # @staticmethod
  # def get_one_ingredient(id):
  #   return Ingredient.query.get(id)

  def __repr(self):
    return '<id {}>'.format(self.id)

  def __repr(self):
    return '<id {}>'.format(self.id)

class IngredientSchema(Schema):
  class Meta:
    model = Ingredient

  id = fields.Int(dump_only=True)
  name = fields.String(required=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)