from typing import List
from fastapi import APIRouter, Depends, status
from schemas import ShowBlog, Blog, BlogUpdate, User
from sqlalchemy.orm import Session
from database import get_db
from repository import blog
from oauth2 import get_current_user

router = APIRouter(prefix='/blog', tags=['Blogs'])

@router.get('/', response_model = List[ShowBlog])
def all(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.create_one(request, db)


@router.get('/{id}', status_code=200, response_model=ShowBlog)
def show(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.delete_one(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: BlogUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.update_one(id, request, db)     