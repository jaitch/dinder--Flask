from textblob import TextBlob
# I tried out TextBlob's other noun phrases chunker implementation, but it was not as good for this purpose

# source: https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/

noise_list = ["additional", "and", "bag", "bags", "beaten", "blanched", "boiled", "boneless", "bottle", "bottled", "breast", "breasts", "cans", "chopped", "cold", "cooked", "cooking", "chunks", "crushed", "cubed", "cup", "cups", "dash", "dashes", "deveined", "diced", "diced", "drained", "dry", "etc", "etc.", "extra", "finely", "firmly packed", "for", "fresh", "freshly", "freshly grated", "frozen", "garnish", "grams", "grated", "ground", "halved", "halves", "hard-boiled", "heaping", "hot", "juiced", "jumbo", "kosher", "large", "leaves", "liquid", "loaf", "medium", "medium-sized", "melted", "minced", "mixed", "more if needed", "needed", "oil", "or", "ounce", "ounces", "oz", "package", "pancake", "peel", "peeled", "pieces", "pitted", "pound", "pounds", "puree", "pureed", "quart", "quartered", "quarters", "quarts", "regular-sized", "rinsed", "salt", "sauce", "sauces", "several", "size", "skinless", "sliced", "slices", "slightly", "small", "softened", "splashing", "sprigs", "stick", "tablespoon", "tablespoons", "taste", "teaspoon", "teaspoons", "the", "thigh", "thighs", "thin", "thinly", "to taste", "torn", "uncooked", "used", "very", "warm", "warmed", "water", "weight", "whole", "your", "zest"]

# olive appearing for olive oil, adjectives that are also nouns

def _remove_noise(input_text):
    words = input_text.split()
    noise_free_words = [word for word in words if word not in noise_list]
    noise_free_text = " ".join(noise_free_words)
    return noise_free_text

blob = TextBlob("1 pound Pasta\n2 Tablespoons Olive Oil\n2 Tablespoons Butter\n1 whole Medium Onion, Chopped Finely\n2 cloves (to 3 Cloves) Garlic, Chopped\n3/4 cups (to 1 Cup) Vodka\n1 can (About 14 Oz.) Tomato Puree\n1 cup Heavy Cream\n1 pinch Red Pepper Flakes\n1/4 teaspoon (to 1/2 Teaspoon) Salt\n Freshly Ground Black Pepper, To Taste\n1 cup Grated Parmesan Cheese")

wordList = []
for np in blob.noun_phrases:
  noise_removed_np = _remove_noise(np)
  if noise_removed_np != '':
    wordList.append(noise_removed_np)
print(list(set(wordList)))
