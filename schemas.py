from pydantic import BaseModel
from typing import Optional


class StudentModel(BaseModel):
    id = int
    firstname: str
    lastname: str
    email: str

class TeacherModel(BaseModel):
    id = int
    firstname: str
    lastname: str
    password: str
    department: Optional[str] = None