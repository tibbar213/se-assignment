from flask import Blueprint, request, jsonify
from app.models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['POST'])
def register():
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

    return jsonify({"msg": "User registered successfully"}), 201


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity={'username': user.username, 'user_type': user.user_type})
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Invalid credentials"}), 401
