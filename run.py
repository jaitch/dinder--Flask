import os

from src.app import create_app

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

app.run()