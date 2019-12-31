import json
from src.models import db
from src.models.RawDataModel import RawDataModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://janicehuang@localhost/dinder')
Session = sessionmaker(bind=engine)
session = Session()

with open("/Users/janicehuang/Downloads/rawRecipeData.json") as json_file:
  for recipe in json_file:
    newRecipe = json.loads(recipe)
    row = RawDataModel(newRecipe)
    session.add(row)
  session.commit()
