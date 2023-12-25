import os

from flask import Flask, request, redirect, make_response 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import abort
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

load_dotenv()
from db import db
from resources.book import book_B as book_blueprint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

SWAGGER_URL = '/help'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/openapi.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Book Inventory API"
    }    
)
app.register_blueprint(book_blueprint)
app.register_blueprint(swaggerui_blueprint)

db.init_app(app)
migrate = Migrate(app, db) 

@app.route('/')
def hello():
	return redirect("/help")#{"book": "API"}

if __name__ == '__main__':
    app.run(debug=True)