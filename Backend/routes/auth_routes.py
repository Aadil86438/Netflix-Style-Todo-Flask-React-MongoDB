from flask import Blueprint, request, jsonify
from models.user_model import create_user, validate_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    success, message = create_user(username, password)
    status_code = 201 if success else 400
    return jsonify({"message": message}), status_code

@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if validate_user(username, password):
        return jsonify({"message": "Login successful", "username": username}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
