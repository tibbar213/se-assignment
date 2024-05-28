from flask import Blueprint, request, jsonify
from app.models import Course
from app import db
from flask_jwt_extended import jwt_required

bp = Blueprint('courses', __name__)


@bp.route('/courses', methods=['POST'])
@jwt_required()
def add_course():
    data = request.get_json()
    course = Course(
        course_name=data.get('course_name'),
        course_code=data.get('course_code'),
        course_description=data.get('course_description'),
        instructor=data.get('instructor'),
        credits=data.get('credits'),
        start_time=data.get('start_time'),
        max_students=data.get('max_students')
    )
    db.session.add(course)
    db.session.commit()
    return jsonify({"msg": "Course added successfully"}), 201


@bp.route('/courses/<int:course_id>', methods=['PUT'])
@jwt_required()
def update_course(course_id):
    data = request.get_json()
    course = Course.query.get_or_404(course_id)

    course.course_name = data.get('course_name', course.course_name)
    course.course_code = data.get('course_code', course.course_code)
    course.course_description = data.get('course_description', course.course_description)
    course.instructor = data.get('instructor', course.instructor)
    course.credits = data.get('credits', course.credits)
    course.start_time = data.get('start_time', course.start_time)
    course.max_students = data.get('max_students', course.max_students)

    db.session.commit()
    return jsonify({"msg": "Course updated successfully"}), 200


@bp.route('/courses/<int:course_id>', methods=['DELETE'])
@jwt_required()
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({"msg": "Course deleted successfully"}), 200


@bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return jsonify({
        'course_id': course.course_id,
        'course_name': course.course_name,
        'course_code': course.course_code,
        'course_description': course.course_description,
        'instructor': course.instructor,
        'credits': course.credits,
        'start_time': course.start_time,
        'max_students': course.max_students
    })


@bp.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{
        'course_id': course.course_id,
        'course_name': course.course_name,
        'course_code': course.course_code,
        'course_description': course.course_description,
        'instructor': course.instructor,
        'credits': course.credits,
        'start_time': course.start_time,
        'max_students': course.max_students
    } for course in courses])

