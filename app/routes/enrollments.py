from flask import Blueprint, request, jsonify, send_file
from app.services.enrollment_service import enroll_course, drop_course, get_enrollments, get_all_enrollments
from flask_jwt_extended import jwt_required, get_jwt_identity
from io import BytesIO
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

bp = Blueprint('enrollments', __name__)

@bp.route('', methods=['POST'])
@jwt_required()
def enroll_course_route():
    identity = get_jwt_identity()
    student_id = identity.get('user_id')
    data = request.get_json()
    course_id = data.get('course_id')
    try:
        enrollment = enroll_course(student_id, course_id)
        return jsonify({"msg": "Enrolled in course successfully", "enrollment": enrollment.course_id}), 201
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400

@bp.route('/<int:course_id>', methods=['DELETE'])
@jwt_required()
def drop_course_route(course_id):
    identity = get_jwt_identity()
    student_id = identity.get('user_id')
    try:
        drop_course(student_id, course_id)
        return jsonify({"msg": "Dropped course successfully"}), 200
    except ValueError as e:
        return jsonify({"msg": str(e)}), 404

@bp.route('', methods=['GET'])
@jwt_required()
def get_enrollments_route():
    identity = get_jwt_identity()
    student_id = identity.get('user_id')
    enrollments = get_enrollments(student_id)
    return jsonify([{
        'enrollment_id': enrollment.enrollment_id,
        'course_id': enrollment.course_id,
        'enrollment_date': enrollment.enrollment_date
    } for enrollment in enrollments])

@bp.route('/export/<string:file_format>', methods=['GET'])
@jwt_required()
def export_enrollments_route(file_format):
    enrollments = get_all_enrollments()
    data = [{
        'student_id': enrollment.student_id,
        'course_id': enrollment.course_id,
        'enrollment_date': enrollment.enrollment_date
    } for enrollment in enrollments]

    if file_format == 'excel':
        df = pd.DataFrame(data)
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Enrollments')
        output.seek(0)
        return send_file(output, attachment_filename='enrollments.xlsx', as_attachment=True)

    elif file_format == 'pdf':
        output = BytesIO()
        p = canvas.Canvas(output, pagesize=letter)
        width, height = letter

        p.drawString(100, height - 100, "Enrollments Report")
        y = height - 130
        for item in data:
            p.drawString(100, y, f"Student ID: {item['student_id']}, Course ID: {item['course_id']}, Enrollment Date: {item['enrollment_date']}")
            y -= 20

        p.showPage()
        p.save()
        output.seek(0)
        return send_file(output, attachment_filename='enrollments.pdf', as_attachment=True)

    else:
        return jsonify({"msg": "Invalid file format"}), 400
