from sqlalchemy.orm import Session
from schemas import StudentModel, TeacherModel
from models import DBTeacher
from hash import Hash


def create_teacher(request: TeacherModel , db: Session):
    new_teacher = DBTeacher(
        firstname = request.firstname,
        lastname = request.lastname,
        password = Hash(request.password),
        department = request.department
    )
    
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher