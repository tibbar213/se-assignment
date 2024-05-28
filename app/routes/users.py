from flask import Blueprint, request, jsonify
from app.models import User, Student
from app import db
from flask_jwt_extended import jwt_required

bp = Blueprint('users', __name__)


@bp.route('/users', methods=['POST'])
@jwt_required()
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user_type = data.get('user_type')

    if not username or not password or not user_type:
        return jsonify({"msg": "Missing required fields"}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, user_type=user_type)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User created successfully"}), 201


@bp.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    data = request.get_json()
    user = User.query.get_or_404(user_id)

    user.username = data.get('username', user.username)
    user.user_type = data.get('user_type', user.user_type)

    if data.get('password'):
        user.password = generate_password_hash(data.get('password'))

    db.session.commit()
    return jsonify({"msg": "User updated successfully"}), 200


@bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"msg": "User deleted successfully"}), 200


@bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        'user_id': user.user_id,
        'username': user.username,
        'user_type': user.user_type
    })


@bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify([{
        'user_id': user.user_id,
        'username': user.username,
        'user_type': user.user_type
    } for user in users])
