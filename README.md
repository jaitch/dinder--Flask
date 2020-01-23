# dinder
Ingredient Matchmaker (Capstone Project)

Pipenv install: Flask, CORS, text, json, pandas, squareform, pdist, numpy, psycopg2, sqlachemy, sqlalcehmy.orm, sqlachemy.types, textblob, re  
Deployed on Heroku: https://dinder-flask.herokuapp.com/
Database plan: Hobby-basic postgresql-curly-46952


Sources:
https://www.codementor.io/@olawalealadeusi896/restful-api-with-python-flask-framework-and-postgres-db-part-1-kbrwbygx5 (Flask skeleton)
https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/ (text cleaning)

173278 recipes

https://open.blogs.nytimes.com/2015/04/09/extracting-structured-data-from-recipes-using-conditional-random-fields
"The most challenging aspect of the recipe parsing problem is the task of predicting ingredient components from the ingredient phrases. Recipes display ingredients like “1 tablespoon fresh lemon juice,” but the database stores ingredients broken down by name (“lemon juice”), quantity (“1″) , unit (“tablespoon”) and comment (“fresh”). There is no regular expression clever enough to identify these labels from the ingredient phrases.

Example
Ingredient Phrase	1	tablespoon	fresh	lemon	juice
Ingredient Labels	QUANTITY	UNIT	COMMENT	NAME	NAME
This type of problem is referred to as a structured prediction problem because we are trying to predict a structure — in this case a sequence of labels — rather than a single label. Structured prediction tasks are difficult because the choice of a particular label for any one word in the phrase can change the model’s prediction of labels for the other words. The added model complexity allows us to learn rich patterns about how words in a sentence interact with the words and labels around them."
