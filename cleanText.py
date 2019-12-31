from textblob import TextBlob
# from textblob.np_extractors import ConllExtractor
# extractor = ConllExtractor()
# tried out TextBlob's other noun phrases chunker implementation, but not as good for this purpose [after quoted blob ->, np_extractor=extractor]


# source: https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/

noise_list = ["cup", "cups", "whole", "teaspoon", "teaspoons", "tablespoon", "tablespoons", "pound", "pounds", "or", "and", "bag", "bags", ", to taste", "for", "several", "dash", "dashes", "thinly", "sliced", "slices", "fresh", "grated", "(additional)", "ounce", "ounces", "grams", "weight", "quart", "quarts", "etc.", ", diced", "chopped", "more if needed", "halved", "dry", "leaves", "package", "small", "large", "stick", "ground", "finely", "minced", "sprigs", "loaf", "firmly packed", "freshly grated", "cold", "warm", "very", "garnish", "salt"]

def _remove_noise(input_text):
    words = input_text.split()
    noise_free_words = [word for word in words if word not in noise_list]
    noise_free_text = " ".join(noise_free_words)
    return noise_free_text

blob = TextBlob("12 ounces, weight Semi-Sweet Chocolate Chips\n4 whole Eggs\n1 Tablespoon Grand Marnier, More To Taste\n1 dash Salt\n1 cup Very Hot Strong Coffee\n Fresh Whipped Cream, For Serving\n Thinly Sliced Orange Peel, For Garnish")

wordList = []
for np in blob.noun_phrases:
  if np != '':
    wordList.append(_remove_noise(np))

print(wordList)
