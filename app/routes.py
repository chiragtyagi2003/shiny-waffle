from flask import jsonify
from app import app

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Email Automation Backend"}), 200
