import pandas as pd
import psycopg2
from sqlalchemy import create_engine

engine = create_engine('postgres+psycopg2://janicehuang@localhost/dinder')

# Method to compute Jaccard similarity index between two sets
def compute_jaccard(ing1_recipes, ing2_recipes):
    intersection = ing1_recipes.intersection(ing2_recipes)
    union = ing1_recipes.union(ing2_recipes)
    jaccard = len(intersection)/float(len(union))
    return jaccard

sql = 'select i.ingredient_id, ri.recipe_id from (select ri.ingredient_id from ingredients i, recipe_ingredients ri where i.id=ri.ingredient_id group by ri.ingredient_id having count(ri.ingredient_id)>5000) as i, recipe_ingredients as ri where i.ingredient_id=ri.ingredient_id'

df = pd.read_sql_query(sql, con=engine, index_col='ingredient_id', coerce_float=False, params=None, parse_dates=None, chunksize=500)

print(df)