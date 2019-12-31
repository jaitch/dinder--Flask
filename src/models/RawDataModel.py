from marshmallow import fields, Schema
import datetime
from . import db
from sqlalchemy.dialects.postgresql import JSONB

class RawDataModel(db.Model):
  """
  Raw Data Model
  """

  __tablename__ = 'rawData'

  id = db.Column(db.Integer, primary_key=True, nullable=False)
  allData = db.Column(JSONB, nullable=False)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    self.allData = data
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  def __repr(self):
    return '<id {}>'.format(self.id)

# class RawDataSchema(Schema):
#   """
#   Raw Data Schema
#   """
#   id = fields.Int(dump_only=True)
#   allData = fields.JSONB(required=True)
#   created_at = fields.DateTime(dump_only=True)
#   modified_at = fields.DateTime(dump_only=True)