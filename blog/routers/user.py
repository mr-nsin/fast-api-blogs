from fastapi import APIRouter, Depends
from schemas import User, ShowUser
from database import get_db
from sqlalchemy.orm import Session
from repository import user

router = APIRouter(prefix='/user', tags=['Users'])


@router.post('/', response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get('/{id}', response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)