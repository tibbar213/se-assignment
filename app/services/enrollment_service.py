from app.models import Enrollment, Course
from app import db
from datetime import datetime


def enroll_course(student_id, course_id):
    course = Course.query.get_or_404(course_id)

    if Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first():
        raise ValueError("Already enrolled in this course")

    if Enrollment.query.filter_by(course_id=course_id).count() >= course.max_students:
        raise ValueError("Course is full")

    enrollment = Enrollment(student_id=student_id, course_id=course_id, enrollment_date=datetime.utcnow())
    db.session.add(enrollment)
    db.session.commit()
    return enrollment


def drop_course(student_id, course_id):
    enrollment = Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first()
    if not enrollment:
        raise ValueError("Not enrolled in this course")

    db.session.delete(enrollment)
    db.session.commit()


def get_enrollments(student_id):
    return Enrollment.query.filter_by(student_id=student_id).all()


def get_all_enrollments():
    return Enrollment.query.all()
