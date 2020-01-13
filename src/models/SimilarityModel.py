from flask import Flask, jsonify
from marshmallow import fields, Schema
import datetime
from . import db

class Similarity(db.Model):

  __tablename__ = 'similarities'

  id = db.Column(db.Integer, primary_key=True)
  source = db.Column(db.String, nullable=False)
  target = db.Column(db.String, nullable=False)
  strength = db.Column(db.Float, nullable=False)

  def __init__(self, data):
    self.source = data.get('source')
    self.source = data.get('target')
    self.source = data.get('strength')

class SimilaritySchema(Schema):
  class Meta:
    model = Similarity

  id = fields.Int(dump_only=True)
  source = fields.String(required=True)
  target = fields.String(required=True)
  strength = fields.String(required=True)
