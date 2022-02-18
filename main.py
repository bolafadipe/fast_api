from fastapi import Depends, FastAPI, status, Response
from typing import Optional
from config import settings
from db.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
from routers import students, teachers


Base.metadata.create_all(engine)


description = """
### This is the API of the school application.
It will contain routes to ;
 - **create**
 - **read**
 - **update** 
 - **delete**  

entities such as students, teachers, admin.
"""

# tags = [
#     {
#         "name":"Students",
#         "description": "these are my students-related routes"
#     },
#     {
#         "name":"Teachers",
#         "description": "these are my teachers-related routes"
#     }
# ]

app = FastAPI(title='My APPLICATION API', description=description, version='0.1.0', contact= {
    'name': 'Bola',
    'email': 'bolafadipe17@gmail.com',
    'website':'bolafad.uk',
},
#openapi_tags=tags
)

app.include_router(students.router)
#app.include_router(teachers.router)


# create root path

@app.get('/', tags=['Home'])
async def root():
    return {'message': 'hello fastapi!'}


# create teachers' path

@app.get('/teachers', tags=['Teachers'])
async def teachers(department: Optional[str]=None):
    return {'message': f'hello teachers in {department} department'}

@app.get('/envvar', tags=['Environment variables'])
async def get_envvar():
    return {'database': settings.DATABASE_URL}

