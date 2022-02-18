from sqlalchemy import Column
from db.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
#from sqlalchemy.orm import relationship

class DBStudent(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    firstname =  Column(String, index=True)
    lastname = Column(String)
    email = Column(String, unique=True, index=True)


class DBTeacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    firstname =  Column(String, index=True)
    lastname =  Column(String, index=True)
    email = Column(String)
    password = Column(String)
    department = Column(String, nullable=True)

class DBAdmin(Base):
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True, index=True)
    department =  Column(String, index=True)
    name = Column(String)



