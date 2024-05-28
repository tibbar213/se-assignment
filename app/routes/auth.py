from flask import Blueprint, request, jsonify
from app.services.auth_service import register_user, authenticate_user

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        new_user = register_user(data['username'], data['password'], data['user_type'])
        return jsonify({"msg": "User registered successfully", "user": new_user.username}), 201
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        access_token = authenticate_user(data['username'], data['password'])
        return jsonify(access_token=access_token), 200
    except ValueError as e:
        return jsonify({"msg": str(e)}), 401
