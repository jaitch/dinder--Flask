import os
from flask_script import Manager
from flask.cli import FlaskGroup
from flask_migrate import Migrate, MigrateCommand
from src.app import create_app, db

env_name = 'development'#os.getenv('FLASK_ENV')
app = create_app(env_name)
cli = FlaskGroup(app)

# migrate = Migrate(app=app, db=db, compare_type=True)

# manager = Manager(app=app)

# manager.add_command('db', MigrateCommand)

# if __name__ == '__main__':
#   manager.run()

@cli.command("create_db")
def create_db():
  db.init_app(app)
  db.drop_all()
  db.create_all()
  db.session.commit()

if __name__ == '__main__':
  cli()
  