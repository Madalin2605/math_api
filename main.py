from flask import Flask
from app.routes.math_routes import math_bp
from app.routes.web_routes import web_bp
# from flask_sqlalchemy import SQLAlchemy
from app.models.db import db


def create_app():
    app = Flask(__name__)

    # DB Config (using SQLite)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///requests.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(math_bp)
    app.register_blueprint(web_bp)

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
