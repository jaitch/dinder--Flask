# dinder
Ingredient Matchmaker (Capstone Project)

Pipenv install: Flask, CORS, text, json, pandas, squareform, pdist, numpy, psycopg2, sqlachemy, sqlalcehmy.orm, sqlachemy.types, textblob, re      

Toggle server in run.py  

To run locally: 
FLASK_ENV=development DATABASE_URL=postgres://janicehuang:localhost/dinder python run.py  

Deployed on Heroku: https://dinder-flask.herokuapp.com/
Database plan: Hobby-basic postgresql-curly-46952

173,278 recipes  
44,197 ingredients  
876,434 ingredient-recipe pairs  
Jaccard Index  
Limited to ingredients with over 1,000 recipes, limited those to 40,000 ingredient-recipe pairs  
18,769 similarities  
call those over .01 (or greater depending on slider)  
