from flask import request, jsonify
from firebase_admin import auth
from app.auth import auth_bp

# Register a new user
@auth_bp.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')

    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        return jsonify({"message": "User created successfully", "uid": user.uid}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Login an existing user
@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    try:
        user = auth.get_user_by_email(email)
        # In a real application, you would verify the password here
        return jsonify({"message": "User logged in successfully", "uid": user.uid}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

