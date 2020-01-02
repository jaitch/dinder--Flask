from textblob import TextBlob
# I tried out TextBlob's other noun phrases chunker implementation, but it was not as good for this purpose

# source: https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/

noise_list = ["additional", "and", "bag", "bags", "blanched", "boiled", "chopped", "cold", "cubed", "cup", "cups", "dash", "dashes", "diced", "diced", "drained", "dry", "etc.", "finely", "firmly packed", "for", "fresh", "freshly grated", "frozen", "garnish", "grams", "grated", "ground", "halved", "hard-boiled", "large", "leaves", "liquid", "loaf", "minced", "mixed", "more if needed", "needed", "or", "ounce", "ounces", "oz", "package", "peeled", "pieces", "pitted", "pound", "pounds", "quart", "quarts", "rinsed", "salt", "several", "size", "sliced", "slices", "small", "splashing", "sprigs", "stick", "tablespoon", "tablespoons", "taste", "teaspoon", "teaspoons", "the", "thinly", "to taste", "torn", "used", "very", "warm", "warmed", "weight", "whole", "your"]

def _remove_noise(input_text):
    words = input_text.split()
    noise_free_words = [word for word in words if word not in noise_list]
    noise_free_text = " ".join(noise_free_words)
    return noise_free_text

blob = TextBlob("2 Tablespoons Olive Oil\n2 Tablespoons Butter\n1 pound Scallops\n1 pound Shrimp\n5 cloves Garlic\n3/4 cups Dry White Wine\n28 ounces, weight Whole Or Diced Tomatoes\n Salt And Pepper, to taste\n1/4 teaspoon Crushed Red Pepper\n1/4 cup Heavy Cream, Warmed\n12 whole Basil Leaves Torn\n Chicken Broth, If Needed For Splashing In A Little Liquid\n12 ounces, weight Pasta (I Used Fusilli Bucati, But Any Kind Will Do!)")

wordList = []
for np in blob.noun_phrases:
  noise_removed_np = _remove_noise(np)
  if noise_removed_np != '':
    wordList.append(noise_removed_np)
print(wordList)
