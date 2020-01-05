from app.api import bp

@bp.route('/recipes/<int:id>', methods=['GET'])

@bp.route('/recipes', methods=['GET'])
def get_recipes():
    pass

def get_recipe(id):
    pass

