from flask import Blueprint, request, jsonify
from app.models import ClassInfo, Course
from app import db
from flask_jwt_extended import jwt_required

bp = Blueprint('class_info', __name__)


@bp.route('/class_info', methods=['POST'])
@jwt_required()
def add_class_info():
    data = request.get_json()
    class_info = ClassInfo(
        course_id=data.get('course_id'),
        student_type=data.get('student_type'),
        year_limit=data.get('year_limit')
    )
    db.session.add(class_info)
    db.session.commit()
    return jsonify({"msg": "Class info added successfully"}), 201


@bp.route('/class_info/<int:class_id>', methods=['PUT'])
@jwt_required()
def update_class_info(class_id):
    data = request.get_json()
    class_info = ClassInfo.query.get_or_404(class_id)

    class_info.course_id = data.get('course_id', class_info.course_id)
    class_info.student_type = data.get('student_type', class_info.student_type)
    class_info.year_limit = data.get('year_limit', class_info.year_limit)

    db.session.commit()
    return jsonify({"msg": "Class info updated successfully"}), 200


@bp.route('/class_info/<int:class_id>', methods=['DELETE'])
@jwt_required()
def delete_class_info(class_id):
    class_info = ClassInfo.query.get_or_404(class_id)
    db.session.delete(class_info)
    db.session.commit()
    return jsonify({"msg": "Class info deleted successfully"}), 200


@bp.route('/class_info/<int:class_id>', methods=['GET'])
@jwt_required()
def get_class_info(class_id):
    class_info = ClassInfo.query.get_or_404(class_id)
    return jsonify({
        'class_id': class_info.class_id,
        'course_id': class_info.course_id,
        'student_type': class_info.student_type,
        'year_limit': class_info.year_limit
    })


@bp.route('/class_info', methods=['GET'])
@jwt_required()
def get_class_infos():
    class_infos = ClassInfo.query.all()
    return jsonify([{
        'class_id': class_info.class_id,
        'course_id': class_info.course_id,
        'student_type': class_info.student_type,
        'year_limit': class_info.year_limit
    } for class_info in class_infos])
