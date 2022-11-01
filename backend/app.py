from flask import Flask, Blueprint
from flask_cors import CORS
#from database.db import get_connection
from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime
#from controladores.Producto import main
from controladores.Producto import mainP
from controladores.Orden import mainO

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost/python_flask_rest"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db=SQLAlchemy(app)
CORS(app)

#from controladores.Producto import *
#from controladores.Orden import *

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

if __name__ == '__main__':
    #app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(mainP, url_prefix='/api')
    app.register_blueprint(mainO, url_prefix='/api')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)