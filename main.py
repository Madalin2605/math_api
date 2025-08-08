from flask import Flask
from app.routes.math_routes import math_bp
from app.routes.web_routes import web_bp
from app.models.db import db
from flask import render_template_string


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

    @app.route("/")
    def landing():
        return render_template_string("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Welcome to Math API</title>
                                <link href="
                https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
                rel="stylesheet">
            </head>
            <body class="bg-light text-center p-5">
                <div class="container">
                    <h1 class="display-4 text-success mb-4">🧮 Welcome to the
                                      Math API</h1>
                    <p class="lead mb-4">
                        Click the button below to access the Web
                        Interface.
                    </p>
                    <a href="/web/" class="btn btn-success btn-lg">
                        Launch Interface
                    </a>
                </div>
            </body>
            </html>
        """)

    app.run(debug=True)
