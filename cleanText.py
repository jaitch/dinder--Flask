from src.models.RawDataModel import RawDataModel
from src.models.IngredientModel import Ingredient
from textblob import TextBlob
from textblob import Word
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
  # no_symbols = re.sub(r'[%/*+_`]', ' ', no_newlines)
  prerinsed_text = re.sub(r'[\d]|[^a-zA-Z-;]', ' ', no_newlines)

  return prerinsed_text

def remove_noise(input_text):

  noise_list = ["-", "®", "-¼", "¼", "-½", "½", "-¾", "¾", "⅓", "'ll", "'s", "...", "-cup", "-diameter", "-inch", "-inch-long", "-inch-wide", "-inch-high", "-inch-diameter", "-inch-thick", "-lb", "-ml", "-ounce", "-ounces", "-oz", "-percent", "-pound", "-quart", "-tablespoon", "-teaspoon", "-thick", "-to", "a", "about", "above", "accent", "accompaniment", "accompaniments", "according", "action", "active", "actual", "adapted", "added","adjust", "adjustable", "adult", "an", "additional", "african", "aged", "ahi", "aisle", "aka", "alaskan", "albacore", "all-natural", "almost-ripe", "alternative", "aluminum", "american", "amount", "and", "and/or", "any", "approx", "approximately", "aromatic", "artisan", "artisan-style", "asian", "assembly", "assorted", "atlantic", "australian", "authentic", "available", "average", "baby", "bag", "bags", "baked", "baker", "baking", "ball", "balls", "base", "basic", "basket", "baste", "basting", "batch", "baton", "batons", "batter", "be", "beaten", "beautiful", "belgian", "below", "best-quality", "big", "bit", "bite", "bite-size", "bite-sized", "bits", "black", "blanched", "blend", "blender", "block", "board" "boiled", "boiling", "bone", "bones", "bone-in", "boneless", "bottle", "bottles", "bottled", "bottom", "bought", "bowl", "bowls", "box", "boxes", "braeburn", "bramley", "branch", "branches", "brand", "bread-and-butter", "breakfast", "breakstone", "breast", "breasts", "brewed", "brick", "bright", "british", "broken", "broken-up", "brown", "browned", "brush", "brushing", "bulb", "bulbs", "bulk", "bunch", "bunches", "bundle", "burrito", "button", "buy", "c", "c.", "california", "calorie", "calories", "campbell's", "can", "canadian", "cane", "canned", "canning", "canola", "cans", "cap", "capacity", "carton", "cartons", "casings", "casserole", "caster", "caught", "cedar", "celtic", "center", "center-cut", "certified", "cheap", "chiffonade", "chilled", "chopped", "chunk", "chunks", "clove", "coins", "cold", "container", "containers", "cooked", "cooking", "cool", "cooled", "cored", "country", "country-style", "chinese", "chips", "choice", "choose", "christmas", "chunk", "chunks", "chunky", "circles", "circular", "classic", "classico", "clean", "cleaned", "clear", "cm", "coarse", "coarse-ground", "coarsely", "coat", "coating", "cob", "cobs", "cocktail", "color", "coloring", "colored", "colossal", "colour", "colouring", "combination", "commercial", "common", "complete", "completely", "concentrate", "concentrated", "cook", "count", "couple", "cracked", "cream-style", "creamy", "crisp", "crispy", "crosswise", "crown", "crumb", "crumbs", "crumbled", "crunch", "crunchy", "crushed", "crust", "crustless", "crusty", "crystal", "cube", "cubed", "cubes", "cup", "cups", "curd", "cut", "cutlets", "cut-up", "dairy", "dairy-free", "dark", "dash", "dashes", "day-old", "deveined", "de-veined", "decoration", "decorative", "decorator", "deep", "dish", "deep-dish", "deep-fry", "defrosted", "degrees", "deli", "deli-style", "delicious", "dense", "depending", "desired", "dessert", "diagonal", "diameter", "dice", "diced", "diced", "diet", "different", "dinner", "dipping", "directions", "discard", "discovery", "disposable", "divided", "dl", "dog", "dole", "double", "double-crust", "dough", "dozen," "dozens" "drained", "dressing", "dried", "drink", "drippings", "drizzle", "drizzling", "drop", "drops", "dry", "dust", "dutch", "dutch-process", "dutch-processed", "each", "ear", "ears", "easy", "eat", "eating", "edible", "edward", "eg", "either", "empire", "empty", "ends", "english", "enough", "entire", "envelope", "equal", "equipment", "equivalent", "essence", "etc", "etc.", "european", "example", "excess", "extra", "extra-firm", "extra-large", "extra-lean", "extra-virgin", "extract", "eye", "f", "f.", "fancy", "family", "farm", "farmers", "fashioned", "fast", "fast-action", "fat", "free", "fat-free", "favorite", "favourite", "few", "field", "filet", "fillet", "filets", "fillets", "fill", "filling", "finely", "find", "fine", "fine-grain", "fine-quality", "fine-mesh", "finest", "finger", "finish", "finished", "finishing", "filtered", "fingers", "firm", "firm-ripe", "firm-tart", "firmly", "firmly-packed", "fl", "flakes", "flaky", "flaked", "flat", "flat-leaf", "flatleaf", "flavor", "flavorful", "flavourful", "flavorless", "flavourless", "flavour", "flavored", "floury", "florets", "fluid", "food", "for", "fork", "frank", "free", "free-range", "french", "fresh", "fresh-ground", "freshly-ground", "freshly", "freshly" "fridge", "fried", "fries", "fruity", "fry", "frying", "fuji", "full", "full-fat", "fully", "fully-cooked", "grated", "frozen", "g", "g.", "gala", "gallon", "garden", "garnish", "garnishes", "garnishing", "gel", "gem", "generous", "gf", "giant", "glace", "glacé", "glass", "glasses", "glaze", "globe", "glug", "glugs", "gluten", "gluten-free", "gm", "gms", "gold", "golden", "good", "good-quality", "goodness", "gourmet", "goya", "gr", "grade", "grain", "grainy", "gram", "grams", "granular", "granulated", "granules", "grass-fed", "grated", "grater", "gravy", "grease", "greasing", "great", "greek", "greek-style", "grocers", "ground", "half-moons", "half-rounds", "halved", "halves", "handful", "handfuls", "hard-boiled", "head", "heaping", "higher-welfare", "hot", "inch-thick", "inch-wide", "ingredients", "instant", "intervals", "jam", "jar", "juice", "juiced", "julienne", "jumbo", "kg", "kilogram", "kind", "knob", "kosher", "lardons", "large", "-lean", "leaf", "lean", "leaves", "leftover", "leg", "length", "lengths", "lengthwise", "-less-sodium", "links", "liquid", "liter", "litre", "loaf", "log", "low-fat", "lowfat", "low-salt", "low-sodium", "matchsticks", "meal", "medallions", "medium", "medium-sized", "melted", "minced", "mix", "mixed", "ml", "more if needed", "needed", "nonfat", "non-fat", "non-dairy", "oil", "optional", "or", "organic", "ounce", "ounces", "oz", "package", "packages", "packed", "pan", "pans", "pancake", "parts", "peel", "peeled", "pie", "piece", "pieces", "pinch", "pinches", "pint", "pitted", "plate", "pod", "pods", "pound", "pounds", "powder", "processor", "puree", "pureed", "quality", "quantities", "quantity", "quart", "quartered", "quarters", "quarts", "rack", "racks", "range", "ready-made", "reduced", "reduced-fat", "regular-sized", "ribbon", "ribbons", "rings", "rinsed", "ripe", "round", "rounds", "rustic", "salt", "sauce", "sauces", "scoop", "scoops", "seasoning", "seeds", "segment", "segments", "semi-circles", "serving", "servings", "several", "shanks", "shavings", "sheet", "sheets", "side", "sides", "size", "sized", "skewers", "skinless", "slice", "sliced", "slices", "slightly", "small", "soda", "softened", "splash", "splashing", "spices", "spoonful", "spoonfuls", "sprigs", "springform", "square", "squares", "squeeze", "stalk", "stalks", "stick", "sticks", "store", "store-bought", "strip", "strips", "style", "substitute", "substituted", "sugar", "sugar-free", "supermarkets", "tablespoon", "tablespoons", "tart", "taste", "tbsp", "teaspoon", "teaspoons", "the", "thick", "thigh", "thighs", "thick", "thick-cut", "thickness", "thin", "thinly", "tip", "to taste", "torn", "trimmed", "tsp", "tub", "uncooked", "uniform", "used", "vegetable", "very", "violet", "warm", "warmed", "water", "wedges", "weight", "whites", "whole", "yolk", "you", "you'll", "your", "you're", "zest"]
  # combine/deal with chili, chilli, chile, chillies, chillis, chilies, chiles...same w chipotle ..... chocolate, cacao, cocoa

  words = input_text.split()
  noise_free_words = [word for word in words if word not in noise_list]
  noise_free_text = " ".join(noise_free_words)
  return noise_free_text

def lemmatize_ingredient(single_ingredient):
  words = single_ingredient.split()
  converted_words = [Word(word) for word in words]
  lemmatized_words = [converted_word.lemmatize() for converted_word in converted_words]
  lemmatized_text = " ".join(lemmatized_words)
  return(lemmatized_text)

def clean_text(ingredients_list):
  wordList = []
  prerinsed_ingredients_list = prerinse(ingredients_list)
  blob = TextBlob(prerinsed_ingredients_list)
  for np in blob.noun_phrases:
    noise_removed_np = remove_noise(np)
    lemmatized_np = lemmatize_ingredient(noise_removed_np)
    if lemmatized_np != '':
      wordList.append(lemmatized_np)
  return list(set(wordList))

for recipe in session.query(RawDataModel).all():
  parsed_ingredients = clean_text(recipe.allData["ingredients"])
  # for ingredient in parsed_ingredients:
  #   row = session.query(Ingredient).filter_by(name=ingredient).scalar()
  #   if row is None:
  #     row = Ingredient(ingredient)
  #   recipe.ingredients.append(row)
  # session.commit()
  print(parsed_ingredients)
