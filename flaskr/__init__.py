from flask import Flask
from config import Config


def create_app(class_config=Config):
    app = Flask(__name__)

    app.config.from_object(class_config)

    from flaskr.main.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
