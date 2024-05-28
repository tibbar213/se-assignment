from app.models import User
from app import db
from werkzeug.security import generate_password_hash


def create_user(user_data):
    username = user_data.get('username')
    password = user_data.get('password')
    user_type = user_data.get('user_type')

    if not username or not password or not user_type:
        raise ValueError("Missing required fields")

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, user_type=user_type)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def update_user(user_id, user_data):
    user = User.query.get_or_404(user_id)

    user.username = user_data.get('username', user.username)
    user.user_type = user_data.get('user_type', user.user_type)

    if user_data.get('password'):
        user.password = generate_password_hash(user_data.get('password'))

    db.session.commit()
    return user


def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()


def get_user(user_id):
    return User.query.get_or_404(user_id)


def get_users():
    return User.query.all()
