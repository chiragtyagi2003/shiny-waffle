from flask import Blueprint


db_bp = Blueprint('db', __name__)

from app.db import routes
