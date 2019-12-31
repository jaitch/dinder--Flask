import json
from src.models.RawDataModel import RawDataModel

Session = sessionmaker(bind=engine)
session = Session()

with open('~/Users/janicehuang/Downloads/rawRecipeData.json', 'r') as json_file:
  json_data = json.load(json_file)
  for recipe in json_data():
    row = RawDataModel(recipe)
    session.add(row)

  session.commit()