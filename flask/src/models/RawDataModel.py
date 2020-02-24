from marshmallow import fields, Schema
import datetime
from . import db
from sqlalchemy.dialects.postgresql import JSONB

recipe_ingredients = db.Table('recipe_ingredients',
  db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id')),
  db.Column('recipe_id', db.Integer, db.ForeignKey('raw_data.id'))
)

class RawDataModel(db.Model):
  """
  Raw Data Model
  """

  __tablename__ = 'raw_data'

  id = db.Column(db.Integer, primary_key=True, nullable=False)
  allData = db.Column(JSONB, nullable=False)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)
  ingredients = db.relationship("Ingredient",
    secondary=recipe_ingredients,
    backref="recipes")

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    self.allData = data
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  # @staticmethod
  # def get_all_recipes():
  #   return RawDataModel.query.all()

  # @staticmethod
  # def get_one_recipe(id):
  #   return RawDataModel.query.get(id)

  # or query.filterby?

  def __repr(self):
    return '<id {}>'.format(self.id)

class RawDataSchema(Schema):
  class Meta:
    model = RawDataModel
#   """
#   Raw Data Schema
#   """
  id = fields.Int(dump_only=True)
  allData = fields.Dict(required=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)

# r = RawDataModel()
# i = Ingredient()
# r.ingredients.append(i)
# db.session.add(r)
# db.session.commit()