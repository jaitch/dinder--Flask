from textblob import TextBlob
# from textblob.np_extractors import ConllExtractor
# extractor = ConllExtractor()
# tried out TextBlob's other noun phrases chunker implementation, but not as good for this purpose [after quoted blob ->, np_extractor=extractor]


# source: https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/

noise_list = ["cup", "cups", "whole", "teaspoon", "teaspoons", "tablespoon", "tablespoons", "pound", "pounds", "or", "and", "bag", "bags", ", to taste", "for", "several", "dash", "dashes", "thinly", "sliced", "slices", "fresh", "grated", "(additional)", "ounce", "ounces", "oz", "grams", "weight", "quart", "quarts", "etc.", ", diced", "chopped", "more if needed", "halved", "dry", "leaves", "package", "small", "large", "stick", "ground", "finely", "minced", "sprigs", "loaf", "firmly packed", "freshly grated", "cold", "warm", "very", "garnish", "salt", "size", "taste", "frozen", "diced", "peeled", "rinsed", "drained", "pitted", "mixed", "cubed", "blanched", "pieces", "the", "your", "boiled", "hard-boiled", "warmed", "torn", "needed", "splashing", "liquid", "used"]

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
