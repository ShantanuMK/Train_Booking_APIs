import sys
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, FastAPI, dependencies
from fastapi.params import Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from internal.user import User
from db.database import engine, SessionLocal
from models import models
from utils.exceptions import APIBaseException
from utils.log_handler import log
import settings
from schema.schema import BookSeat

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/Users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

if settings.DEBUG_LEVEL:
    logger = log(__name__, level="DEBUG")
else:
    logger = log(__name__)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/register/")
def register(username: str, name: str, age_yr: int, address: str, db: Session = Depends(get_db)):
    try:
        return User.register(username, name, age_yr, address, db=db)
    except APIBaseException as ae:
        logger.exception(str(ae))
        raise HTTPException(status_code=ae.code, detail=ae.message)
    except Exception as e:
        logger.exception(str(e))
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/avaliable_coach_seats/")
def avaliable_coach_seats(train_id, coach_type: Optional[str] = Query(None, enum=['A/C Sleeper', 'NON A/C Sleeper', 'SEATER']), coach_num: Optional[int] = None, db: Session = Depends(get_db)):
    try:
        return User.avaliable_coach_seats(train_id, coach_type, coach_num, db=db)
    except APIBaseException as ae:
        logger.exception(str(ae))
        raise HTTPException(status_code=ae.code, detail=ae.message)
    except Exception as e:
        logger.exception(str(e))
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/book_seats/")
def book_seats(userid, train_id, travel_date, data: List[BookSeat],  db: Session = Depends(get_db)):
    try:
        return User.book_seats(userid, train_id, travel_date, data, db=db)
    except APIBaseException as ae:
        logger.exception(str(ae))
        raise HTTPException(status_code=ae.code, detail=ae.message)
    except Exception as e:
        logger.exception(str(e))
        raise HTTPException(status_code=500, detail=str(e))


