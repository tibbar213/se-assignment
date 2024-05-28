from app.models import ClassInfo
from app import db


def add_class_info(class_info_data):
    class_info = ClassInfo(
        course_id=class_info_data.get('course_id'),
        student_type=class_info_data.get('student_type'),
        year_limit=class_info_data.get('year_limit')
    )
    db.session.add(class_info)
    db.session.commit()
    return class_info


def update_class_info(class_id, class_info_data):
    class_info = ClassInfo.query.get_or_404(class_id)

    class_info.course_id = class_info_data.get('course_id', class_info.course_id)
    class_info.student_type = class_info_data.get('student_type', class_info.student_type)
    class_info.year_limit = class_info_data.get('year_limit', class_info.year_limit)

    db.session.commit()
    return class_info


def delete_class_info(class_id):
    class_info = ClassInfo.query.get_or_404(class_id)
    db.session.delete(class_info)
    db.session.commit()


def get_class_info(class_id):
    return ClassInfo.query.get_or_404(class_id)


def get_class_infos():
    return ClassInfo.query.all()
