from textblob import TextBlob
# I tried out TextBlob's other noun phrases chunker implementation, but it was not as good for this purpose

# source: https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/

noise_list = ["additional", "and", "bag", "bags", "blanched", "boiled", "chopped", "cold", "cubed", "cup", "cups", "dash", "dashes", "diced", "diced", "drained", "dry", "etc.", "extra", "finely", "firmly packed", "for", "fresh", "freshly grated", "frozen", "garnish", "grams", "grated", "ground", "halved", "hard-boiled", "heaping", "large", "leaves", "liquid", "loaf", "melted", "minced", "mixed", "more if needed", "needed", "or", "ounce", "ounces", "oz", "package", "pancake", "peeled", "pieces", "pitted", "pound", "pounds", "quart", "quarts", "rinsed", "salt", "several", "size", "sliced", "slices", "small", "splashing", "sprigs", "stick", "tablespoon", "tablespoons", "taste", "teaspoon", "teaspoons", "the", "thinly", "to taste", "torn", "used", "very", "warm", "warmed", "weight", "whole", "your", "zest"]

def _remove_noise(input_text):
    words = input_text.split()
    noise_free_words = [word for word in words if word not in noise_list]
    noise_free_text = " ".join(noise_free_words)
    return noise_free_text

blob = TextBlob("1-1/2 cup Cake Flour\n1 Tablespoon (additional) Cake Flour\n1/4 teaspoon Salt\n1 Tablespoon (heaping) Baking Powder\n3 Tablespoons Sugar\n1-1/2 cup Evaporated Milk (more If Needed)\n1 whole Lemon (more If Needed)\n1 whole Large Egg\n1-1/2 teaspoon Vanilla\n2 Tablespoons Butter, Melted\n Zest From 1 Lemon\n1 cup Heaping Blueberries\n Extra Butter\n Maple Or Pancake Syrup")

wordList = []
for np in blob.noun_phrases:
  noise_removed_np = _remove_noise(np)
  if noise_removed_np != '':
    wordList.append(noise_removed_np)
print(list(set(wordList)))
