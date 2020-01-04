from src.models.RawDataModel import RawDataModel
from src.models.IngredientModel import Ingredient
from textblob import TextBlob
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import re

engine = create_engine('postgresql://janicehuang@localhost/dinder')
Session = sessionmaker(bind=engine)
session = Session()

# I tried out TextBlob's other noun phrases chunker implementation, but it was not as good for this purpose

# source: https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/


  # olive appearing for olive oil, adjectives that are also nouns, cloves the spice vs garlic measurement

def prerinse(input_text):
  no_newlines = re.sub('\\n', '; ', input_text)
  prerinsed_text = re.sub('[%/\d\*\+\[\]-_`]', ' ', no_newlines)
  return prerinsed_text

def remove_noise(input_text):

  noise_list = ["®", "'ll", "'s", "...", "-diameter", "-inch", "-inch-diameter", "-inch-thick", "-ounce", "-percent", "-pound", "-quart", "-tablespoon", "-teaspoon", "-thick", "a", "about", "above", "accent", "accompaniment", "accompaniments", "according", "active", "actual", "adapted", "added","adjust", "adjustable", "adult", "an", "additional", "aged", "ahi", "aka", "al dente", "alaskan", "albacore", "all-natural", "almost-ripe", "alternative", "aluminum", "american", "amount", "and", "and/or", "any", "approx", "approximately", "aromatic", "artisan", "artisan-style", "asian", "assembly", "assorted", "atlantic", "australian", "authentic", "available", "average", "baby", "bag", "bags", "baked", "baker", "baking", "ball", "balls", "base", "basic", "basket", "baste", "basting", "batch", "baton", "batons", "batter", "be", "beaten", "beautiful", "belgian", "below", "best-quality", "big", "bit", "bite", "bite-size", "bite-sized", "bits", "black", "blanched", "blend", "blender", "block", "board" "boiled", "boiling", "bone", "bones", "bone-in", "boneless", "bottle", "bottles", "bottled", "bottom", "bought", "bowl", "bowls", "box", "boxes", "branch", "branches", "brand", "bread-and-butter", "breakfast", "breakstone", "breast", "breasts", "brewed", "brick", "bright", "british", "broken", "broken-up", "brown", "browned", "brush", "brushing", "bulb", "bulbs", "bulk", "bunch", "bunches", "bundle", "burrito", "button", "buy", "c", "c.", "california", "calorie", "calories", "campbell's", "can", "canadian", "cane", "canned", "canning", "canola", "cans", "cap", "capacity", "carton", "cartons", "casings", "casserole", "caster", "caught", "cedar", "celtic", "center", "center-cut", "certified", "cheap", "chiffonade", "chilled", "chopped", "chunk", "chunks", "clove", "coins", "cold", "container", "containers", "cooked", "cooking", "cool", "cooled", "cored", "country", "country-style", "chinese", "chips", "choice", "choose", "christmas", "chunk", "chunks", "chunky", "circles", "circular", "classic", "classico", "clean", "cleaned", "clear", "cm", "coarse", "coarse-ground", "coarsely", "coat", "coating", "cob", "cobs", "cocktail", "color", "coloring", "colored", "colossal", "colour", "colouring", "combination", "commercial", "common", "complete", "completely", "concentrate", "concentrated", "cook", "count", "couple", "cracked", "cream-style", "creamy", "crisp", "crispy", "crosswise", "crown", "crumb", "crumbs", "crumbled", "crunch", "crunchy", "crushed", "crust", "crustless", "crusty", "crystal", "cube", "cubed", "cubes", "cup", "cups", "curd", "cut", "cutlets", "cut-up", "dairy", "dairy-free", "dark", "dash", "dashes", "day-old", "deveined", "de-veined", "decoration", "decorative", "decorator", "deep", "dish", "deep-dish", "deep-fry", "defrosted", "degrees", "deli", "deli-style", "delicious", "dense", "depending", "desired", "dessert", "diagonal", "diameter", "dice", "diced", "diced", "diet", "different", "dinner", "dipping", "directions", "discard", "discovery", "disposable", "divided", "dl", "dog", "dole", "double", "double-crust", "dough", "dozen," "dozens" "drained", "dressing", "dried", "drink", "drippings", "drizzle", "drizzling", "drop", "drops", "dry", "dust", "dutch", "dutch-process", "dutch-processed", "each", "ear", "ears", "easy", "eat", "edible", "edward", "eg", "envelope", "equipment", "essence", "etc", "etc.", "extra", "extra-firm", "fat-free", "filet", "fillet", "filets", "fillets", "filling", "finely", "fingers", "firmly-packed", "flat-leaf", "flavored", "florets", "for", "free-range", "fresh", "freshly", "freshly grated", "frozen", "g", "gallon", "garnish", "gem", "good-quality", "grams", "granules", "grated", "grocers", "ground", "half-moons", "half-rounds", "halved", "halves", "handful", "hard-boiled", "head", "heaping", "hot", "inch-thick", "inch-wide", "ingredients", "instant", "intervals", "jar", "juice", "juiced", "julienne", "jumbo", "kg", "kilogram", "kind", "knob", "kosher", "lardons", "large", "-lean", "lean", "leaves", "leftover", "leg", "length", "lengths", "lengthwise", "-less-sodium", "links", "liquid", "liter", "litre", "loaf", "log", "low-fat", "lowfat", "low-salt", "low-sodium", "matchsticks", "meal", "medallions", "medium", "medium-sized", "melted", "minced", "mix", "mixed", "ml", "more if needed", "needed", "nonfat", "non-fat", "non-dairy", "oil", "optional", "or", "organic", "ounce", "ounces", "oz", "package", "packages", "pan", "pans", "pancake", "peel", "peeled", "pie", "piece", "pieces", "pinch", "pinches", "pint", "pitted", "plate", "pod", "pods", "pound", "pounds", "powder", "puree", "pureed", "quantities", "quantity", "quart", "quartered", "quarters", "quarts", "rack", "racks", "reduced-fat", "regular-sized", "ribbon", "ribbons", "rings", "rinsed", "ripe", "round", "rounds", "rustic", "salt", "sauce", "sauces", "scoop", "scoops", "seasoning", "seeds", "segment", "segments", "semi-circles", "serving", "servings", "several", "shanks", "shavings", "sheet", "sheets", "side", "sides", "size", "sized", "skewers", "skinless", "slice", "sliced", "slices", "slightly", "small", "soda", "softened", "splash", "splashing", "spices", "spoonful", "spoonfuls", "sprigs", "springform", "square", "squares", "stalk", "stalks", "stick", "sticks", "store", "store-bought", "strip", "strips", "style", "substitute", "substituted", "sugar", "supermarkets", "tablespoon", "tablespoons", "taste", "teaspoon", "teaspoons", "the", "thick", "thigh", "thighs", "thick", "thick-cut", "thickness", "thin", "thinly", "tip", "to taste", "torn", "tub", "uncooked", "uniform", "used", "vegetable", "very", "violet", "warm", "warmed", "water", "wedges", "weight", "whole", "you", "you'll", "your", "you're", "zest"]
  # combine/deal with chili, chilli, chile, chillies, chillis, chilies, chiles...same w chipotle ..... chocolate, cacao, cocoa

  words = input_text.split()
  noise_free_words = [word for word in words if word not in noise_list]
  noise_free_text = " ".join(noise_free_words)
  return noise_free_text

def clean_text(ingredients_list):
  wordList = []
  prerinsed_ingredients_list = prerinse(ingredients_list)
  blob = TextBlob(prerinsed_ingredients_list)
  for np in blob.noun_phrases:
    noise_removed_np = remove_noise(np)
    if noise_removed_np != '':
      wordList.append(noise_removed_np)
  # return list(set(wordList))
  print(set(wordList))

# for recipe in session.query(RawDataModel).all():
#   parsed_ingredients = clean_text(recipe.allData["ingredients"])
#   for ingredient in parsed_ingredients:
#     row = session.query(Ingredient).filter_by(name=ingredient).scalar()
#     if row is None:
#       row = Ingredient(ingredient)
#     recipe.ingredients.append(row)
#   session.commit()

clean_text("4 cups Unprepared Rice\n6 cups (to 8 Cups) Low Sodium Chicken Broth/stock\n4 whole (to 8) Tomatoes (up To You)\n2 whole (to 3) Onions (up To You)\n8 cloves (to 14 Cloves) Of Garlic (up To You)\n Butter\n Taco Seasoning (or Chili Powder, Paprika, And Cumin) To Taste\n1 can (to 2 Cans) Black Or Pinto Beans (up To You)\n3 pounds Lean Ground Beef\n2 jars (16 Ounce) Salsa Verde\n Flour Tortillas\n3 packages (16 Ounces) Mexican Cheese Blend\n1 jar (16 Ounce) Enchilada Sauce\n3 cans Corn, Drained\n Sour Cream, to taste\n Cilantro, to taste")
