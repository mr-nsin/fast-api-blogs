from typing import List
from fastapi import APIRouter, Depends
from schemas import ShowBlog
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter()

@router.get('/blog', response_model = List[ShowBlog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs