from flask import Blueprint, request, jsonify, send_file
from app.models import Enrollment, Course
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from io import BytesIO
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

bp = Blueprint('enrollments', __name__)


@bp.route('/enrollments', methods=['POST'])
@jwt_required()
def enroll_course():
    identity = get_jwt_identity()
    student_id = identity.get('user_id')
    data = request.get_json()
    course_id = data.get('course_id')

    course = Course.query.get_or_404(course_id)

    if Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first():
        return jsonify({"msg": "Already enrolled in this course"}), 400

    if Enrollment.query.filter_by(course_id=course_id).count() >= course.max_students:
        return jsonify({"msg": "Course is full"}), 400

    enrollment = Enrollment(student_id=student_id, course_id=course_id, enrollment_date=datetime.utcnow())
    db.session.add(enrollment)
    db.session.commit()

    return jsonify({"msg": "Enrolled in course successfully"}), 201


@bp.route('/enrollments/<int:course_id>', methods=['DELETE'])
@jwt_required()
def drop_course(course_id):
    identity = get_jwt_identity()
    student_id = identity.get('user_id')

    enrollment = Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first()
    if not enrollment:
        return jsonify({"msg": "Not enrolled in this course"}), 404

    db.session.delete(enrollment)
    db.session.commit()

    return jsonify({"msg": "Dropped course successfully"}), 200


@bp.route('/enrollments', methods=['GET'])
@jwt_required()
def get_enrollments():
    identity = get_jwt_identity()
    student_id = identity.get('user_id')

    enrollments = Enrollment.query.filter_by(student_id=student_id).all()
    return jsonify([{
        'enrollment_id': enrollment.enrollment_id,
        'course_id': enrollment.course_id,
        'enrollment_date': enrollment.enrollment_date
    } for enrollment in enrollments])


@bp.route('/enrollments/export/<string:file_format>', methods=['GET'])
@jwt_required()
def export_enrollments(file_format):
    enrollments = Enrollment.query.all()
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
            p.drawString(100, y,
                         f"Student ID: {item['student_id']}, Course ID: {item['course_id']}, Enrollment Date: {item['enrollment_date']}")
            y -= 20

        p.showPage()
        p.save()
        output.seek(0)
        return send_file(output, attachment_filename='enrollments.pdf', as_attachment=True)

    else:
        return jsonify({"msg": "Invalid file format"}), 400
