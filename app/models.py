from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    user_type = db.Column(db.Enum('超级管理员', '管理员', '学生'), nullable=False)
    student = db.relationship('Student', backref='user', uselist=False)

class Student(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    student_number = db.Column(db.String(20), unique=True, nullable=False)
    major = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)

class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    course_code = db.Column(db.String(50), unique=True, nullable=False)
    course_description = db.Column(db.Text)
    instructor = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    max_students = db.Column(db.Integer, nullable=False)
    enrollments = db.relationship('Enrollment', backref='course', lazy=True)

class Enrollment(db.Model):
    enrollment_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)
    enrollment_date = db.Column(db.DateTime, nullable=False)

class ClassInfo(db.Model):
    class_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)
    student_type = db.Column(db.Enum('本科生', '研究生'), nullable=False)
    year_limit = db.Column(db.Integer)
