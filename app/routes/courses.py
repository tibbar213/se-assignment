from flask import Blueprint, request, jsonify
from app.services.course_service import add_course, update_course, delete_course, get_course, get_courses
from flask_jwt_extended import jwt_required

bp = Blueprint('courses', __name__)

@bp.route('/courses', methods=['POST'])
@jwt_required()
def add_course_route():
    data = request.get_json()
    course = add_course(data)
    return jsonify({"msg": "Course added successfully", "course": course.course_name}), 201

@bp.route('/courses/<int:course_id>', methods=['PUT'])
@jwt_required()
def update_course_route(course_id):
    data = request.get_json()
    course = update_course(course_id, data)
    return jsonify({"msg": "Course updated successfully", "course": course.course_name}), 200

@bp.route('/courses/<int:course_id>', methods=['DELETE'])
@jwt_required()
def delete_course_route(course_id):
    delete_course(course_id)
    return jsonify({"msg": "Course deleted successfully"}), 200

@bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course_route(course_id):
    course = get_course(course_id)
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
def get_courses_route():
    courses = get_courses()
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
