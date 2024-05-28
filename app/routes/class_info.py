from flask import Blueprint, request, jsonify
from app.services.class_info_service import add_class_info, update_class_info, delete_class_info, get_class_info, get_class_infos
from flask_jwt_extended import jwt_required

bp = Blueprint('class_info', __name__)

@bp.route('/class_info', methods=['POST'])
@jwt_required()
def add_class_info_route():
    data = request.get_json()
    class_info = add_class_info(data)
    return jsonify({"msg": "Class info added successfully", "class_info": class_info.class_id}), 201

@bp.route('/class_info/<int:class_id>', methods=['PUT'])
@jwt_required()
def update_class_info_route(class_id):
    data = request.get_json()
    class_info = update_class_info(class_id, data)
    return jsonify({"msg": "Class info updated successfully", "class_info": class_info.class_id}), 200

@bp.route('/class_info/<int:class_id>', methods=['DELETE'])
@jwt_required()
def delete_class_info_route(class_id):
    delete_class_info(class_id)
    return jsonify({"msg": "Class info deleted successfully"}), 200

@bp.route('/class_info/<int:class_id>', methods=['GET'])
@jwt_required()
def get_class_info_route(class_id):
    class_info = get_class_info(class_id)
    return jsonify({
        'class_id': class_info.class_id,
        'course_id': class_info.course_id,
        'student_type': class_info.student_type,
        'year_limit': class_info.year_limit
    })

@bp.route('/class_info', methods=['GET'])
@jwt_required()
def get_class_infos_route():
    class_infos = get_class_infos()
    return jsonify([{
        'class_id': class_info.class_id,
        'course_id': class_info.course_id,
        'student_type': class_info.student_type,
        'year_limit': class_info.year_limit
    } for class_info in class_infos])
