from flask import Flask


def create_app():
    app = Flask(__name__)


    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/main')

    return app
