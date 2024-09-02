from flask import Flask
from app.db.mysql_connector import connect_to_database
from app.config import Config

def create_app():
    app = Flask(__name__)


   # Load the configuration from the Config class
    app.config.from_object(Config)

    # Register blueprints for auth
    from app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    # Register blueprints for db
    from app.db.routes import db_bp
    app.register_blueprint(db_bp, url_prefix='/db')

    # Establish a database connection when the app starts
    with app.app_context():
        db_connection = connect_to_database()
        app.config['DB_CONNECTION'] = db_connection

    return app
