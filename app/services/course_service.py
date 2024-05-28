from app.models import Course
from app import db


def add_course(course_data):
    course = Course(
        course_name=course_data.get('course_name'),
        course_code=course_data.get('course_code'),
        course_description=course_data.get('course_description'),
        instructor=course_data.get('instructor'),
        credits=course_data.get('credits'),
        start_time=course_data.get('start_time'),
        max_students=course_data.get('max_students')
    )
    db.session.add(course)
    db.session.commit()
    return course


def update_course(course_id, course_data):
    course = Course.query.get_or_404(course_id)

    course.course_name = course_data.get('course_name', course.course_name)
    course.course_code = course_data.get('course_code', course.course_code)
    course.course_description = course_data.get('course_description', course.course_description)
    course.instructor = course_data.get('instructor', course.instructor)
    course.credits = course_data.get('credits', course.credits)
    course.start_time = course_data.get('start_time', course.start_time)
    course.max_students = course_data.get('max_students', course.max_students)

    db.session.commit()
    return course


def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()


def get_course(course_id):
    return Course.query.get_or_404(course_id)


def get_courses():
    return Course.query.all()
