import sys
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, FastAPI, dependencies
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from crud import crud_user
from db.database import engine, SessionLocal
from models import models
from exceptions.exceptions import UserAlreadyRegistered, UserNotFound

import schema.schema

models.Base.metadata.create_all(bind=engine)
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



