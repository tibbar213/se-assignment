from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models import User
from app import db


def register_user(username, password, user_type):
    if not username or not password or not user_type:
        raise ValueError("Missing required fields")

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, user_type=user_type)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        access_token = create_access_token(
            identity={'user_id': user.user_id, 'username': user.username, 'user_type': user.user_type})
        return access_token
    else:
        raise ValueError("Invalid credentials")
