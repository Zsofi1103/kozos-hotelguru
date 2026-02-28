from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Globális objektumok
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    from .config import db_config
    params = db_config()
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['database']}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'hotelguru_titok'

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import models
        from . import routes

    return app
