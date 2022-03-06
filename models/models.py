from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, Numeric, TIMESTAMP, Text, null, Date
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid
import datetime
from db.database import Base, engine
from sqlalchemy import CheckConstraint

class UsersModel(Base):
	__tablename__ = "users"
	userid = Column(Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
	username = Column(String(20), index=True)
	name = Column(String(20), index=True)
	age_yr = Column(Integer, nullable = False)
	address = Column(String(100), nullable = False)


#seates -> coach-id, train-id, coach-type, coach-num
class SeatsModel(Base):
	__tablename__ = "seats"
	coach_id = Column(Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
	train_id = Column(String(20), index=True)
	coach_type = Column(Integer, nullable = False)
	coach_num = Column(String(100), nullable = False)

class DatesModel(Base):
	__tablename__ = "dates"
	id = Column(Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
	bookingid = Column(Text(length=36))
	coach_id = Column(Text, nullable=False)
	seat_num = Column(Integer, CheckConstraint('seat_num>0'), nullable=False)
	passenger_name = Column(Text, nullable=False)
	passenger_age = Column(Integer, nullable=False)
	travel_date = Column(Date, nullable=False)

class BookingsModel(Base):
	__tablename__ = "bookings"
	bookingid = Column(Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
	userid = Column(Text, nullable=False)
	train_id = Column(Text, nullable=False)
	booking_date = Column(DateTime, default=datetime.datetime.now)


"""
users -> userid, username, name, address
seates -> coach-id, train-id, coach-type, coach-num
dates -> bookingid, coach-id, seat-num, passenger-name, passenger-age, date
bookings -> bookingid, userid, coach-id, seats-num,, datetime
"""