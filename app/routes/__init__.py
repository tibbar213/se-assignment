from flask import Blueprint

# Import the blueprints from each module
from .auth import bp as auth_bp
from .courses import bp as courses_bp
from .enrollments import bp as enrollments_bp
from .users import bp as users_bp
from .class_info import bp as class_info_bp

# Initialize the Blueprint
def init_app(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(courses_bp, url_prefix='/courses')
    app.register_blueprint(enrollments_bp, url_prefix='/enrollments')
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(class_info_bp, url_prefix='/class_info')
