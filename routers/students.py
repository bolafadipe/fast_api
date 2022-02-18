from fastapi import APIRouter
from fastapi import status, Response
from typing import Optional
from schemas import StudentModel

router = APIRouter(prefix='/student', tags=['students'])


# create student
@router.post('/new')
async def create_student(student: StudentModel):
    return 'student created'

# create students' path
@router.get('/all', 
        
        summary="retrieve all students",
        description="a call to this api will retrieve information about all students"
)
async def students(name):
    return {'message': f'hello {name}'}

# complex path & query params
@router.get('/{st_id}/courses/{course_id}')
async def students(st_id:int, course_id:int, name: str, year: Optional[int]=None):
    """
        simulates retrieving students using student id and name as filters.
        Year of study could be passed as an optional query parameter
        - **st_id** mandatory path parameter
        - **year** optional parameter
    """
    return {'message': f'hello {name}'}

# status code validation

@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_student(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'no student with id {id}'}
    else:
        response.status_code = status.HTTP_200_OK
        return 'successful'
