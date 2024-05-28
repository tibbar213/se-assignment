from flask import Blueprint, request, jsonify
from app.services.user_service import create_user, update_user, delete_user, get_user, get_users
from flask_jwt_extended import jwt_required

bp = Blueprint('users', __name__)

@bp.route('/users', methods=['POST'])
@jwt_required()
def create_user_route():
    data = request.get_json()
    try:
        new_user = create_user(data)
        return jsonify({"msg": "User created successfully", "user": new_user.username}), 201
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400

@bp.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user_route(user_id):
    data = request.get_json()
    try:
        user = update_user(user_id, data)
        return jsonify({"msg": "User updated successfully", "user": user.username}), 200
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400

@bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user_route(user_id):
    delete_user(user_id)
    return jsonify({"msg": "User deleted successfully"}), 200

@bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_route(user_id):
    user = get_user(user_id)
    return jsonify({
        'user_id': user.user_id,
        'username': user.username,
        'user_type': user.user_type
    })

@bp.route('/users', methods=['GET'])
@jwt_required()
def get_users_route():
    users = get_users()
    return jsonify([{
        'user_id': user.user_id,
        'username': user.username,
        'user_type': user.user_type
    } for user in users])
