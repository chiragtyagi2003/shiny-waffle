from flask import Flask


def create_app():
    app = Flask(__name__)


    # Register blueprints
    from app.auth.routes import auth_bp

    # Import config.py to initialize Firebase and other services
    from app import config
    
    app.register_blueprint(auth_bp)
  

    return app
