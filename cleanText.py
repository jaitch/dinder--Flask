from src.models.RawDataModel import RawDataModel
from src.models.IngredientModel import Ingredient
from textblob import TextBlob
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://janicehuang@localhost/dinder')
Session = sessionmaker(bind=engine)
session = Session()

# I tried out TextBlob's other noun phrases chunker implementation, but it was not as good for this purpose

# source: https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/


  # olive appearing for olive oil, adjectives that are also nouns, cloves the spice vs garlic measurement

def remove_noise(input_text):

  noise_list = ["additional", "and", "bag", "bags", "beaten", "blanched", "boiled", "boneless", "bottle", "bottled", "breast", "breasts", "cans", "chopped", "cold", "cooked", "cooking", "chunks", "crushed", "cubed", "cup", "cups", "cut", "dash", "dashes", "deveined", "diced", "diced", "drained", "dry", "etc", "etc.", "extra", "finely", "firmly packed", "for", "fresh", "freshly", "freshly grated", "frozen", "garnish", "grams", "grated", "ground", "halved", "halves", "hard-boiled", "heaping", "hot", "juiced", "jumbo", "kosher", "large", "leaves", "liquid", "loaf", "medium", "medium-sized", "melted", "minced", "mixed", "more if needed", "needed", "oil", "or", "ounce", "ounces", "oz", "package", "pancake", "peel", "peeled", "pieces", "pitted", "pound", "pounds", "puree", "pureed", "quart", "quartered", "quarters", "quarts", "regular-sized", "rinsed", "salt", "sauce", "sauces", "seasoning", "several", "size", "skinless", "sliced", "slices", "slightly", "small", "softened", "splashing", "spices", "sprigs", "stick", "strips", "substitute", "tablespoon", "tablespoons", "taste", "teaspoon", "teaspoons", "the", "thigh", "thighs", "thin", "thinly", "to taste", "torn", "uncooked", "used", "vegetable", "very", "warm", "warmed", "water", "weight", "whole", "your", "zest"]

  words = input_text.split()
  noise_free_words = [word for word in words if word not in noise_list]
  noise_free_text = " ".join(noise_free_words)
  return noise_free_text

def clean_text(ingredients_list):
  wordList = []
  blob = TextBlob(ingredients_list)
  for np in blob.noun_phrases:
    noise_removed_np = remove_noise(np)
    if noise_removed_np != '':
      wordList.append(noise_removed_np)
  return list(set(wordList))


for recipe in session.query(RawDataModel).all():
  parsed_ingredients = clean_text(recipe.allData["ingredients"])
  for ingredient in parsed_ingredients:
    row = session.query(Ingredient).filter_by(name=ingredient).scalar()
    if row is None:
      row = Ingredient(ingredient)
    recipe.ingredients.append(row)
  session.commit()
