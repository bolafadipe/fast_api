from fastapi import APIRouter, Depends
from db.database import get_db
from schemas import TeacherModel
from sqlalchemy.orm import Session
from db.teacher import create_teacher
from db import teacher

router = APIRouter(prefix='/student', tags=['students'])

# create teacher endpoint
@router.post()
async def create_teacher_api(request: TeacherModel, db: Session = Depends(get_db)):
    return create_teacher(request, db)