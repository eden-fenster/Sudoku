from flask import *
from web import app1
from processor import app2

app = Flask(__name__)
def create_app():

    # register blueprints
    app.register_blueprint(app1.sudoku_server)
    app.register_blueprint(app2.sudoku_processor)
