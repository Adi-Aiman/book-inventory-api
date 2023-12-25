import os

from flask import Flask, redirect 
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
from dotenv import load_dotenv
from db import db
from resources.book import book_B as book_blueprint
from seed_script import Seeder

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

SWAGGER_URL = '/help'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/openapi.json'  #API url / local resource

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

table_exist = Seeder.validate_table()

with app.app_context():
      db.create_all()

if(not table_exist):
   Seeder.seed_initial_values()

migrate = Migrate(app, db)

@app.route('/')
def hello():
	return redirect("/help")#{"book": "API"}

if __name__ == '__main__':
    app.run(debug=False)