from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import models
from schemas import Blog, BlogUpdate

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create_one(request: Blog, db: Session):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete_one(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with {id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update_one(id: int, request: BlogUpdate, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with {id} not found')
    blog.update(request.dict())
    db.commit()
    return 'done'

def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} is not found in database")
    return blog