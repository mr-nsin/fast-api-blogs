from fastapi import APIRouter, Depends, HTTPException, status
from schemas import Login
from database import get_db
from sqlalchemy.orm import Session
import models

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
    return 'login'