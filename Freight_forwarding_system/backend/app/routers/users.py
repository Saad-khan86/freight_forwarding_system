from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from ..database import get_session
from .. import models

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/new_user", response_model=models.User)
def create_user(user: models.User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh()
    return user

@router.get("/all_user", response_model=list[models.User])
def read_users(session: Session = Depends(get_session)):
    statement = select(models.User)
    alluser = session.exec(statement).all
    return alluser
