from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import sqlalchemy.engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

print(sqlalchemy.__version__)

engine = sqlalchemy.engine.create_engine('postgresql://postgres:postgres@localhost/postgres', echo=True)

Base = declarative_base()


class Hotel(Base):
    __tablename__ = 'hotels'

    hotel_no = Column(Integer, primary_key=True)
    hotel_name = Column(String)
    city_name = Column(String)
    rooms = relationship('Room', backref='rooms', lazy=True)


class Room(Base):
    __tablename__ = 'rooms'

    room_no = Column(Integer, primary_key=True)
    hotel_no = Column(Integer, ForeignKey('hotels.hotel_no'), primary_key=True)
    type = Column(String)
    price = Column(Integer)


class Booking(Base):
    __tablename__ = 'bookings'

    hotel_no = Column(Integer, ForeignKey('hotels.hotel_no'), primary_key=True)
    guest_no = Column(Integer, ForeignKey('guests.guest_no'), primary_key=True)
    date_from = Column(DateTime, primary_key=True)
    room_no = Column(Integer)


class Guest(Base):
    __tablename__ = 'guests'
    guest_no = Column(Integer, primary_key=True)
    guest_name = Column(String)
    guest_address = Column(String)



Base.metadata.create_all(engine)

new_hotel = Hotel(hotel_name='first_hotel', city_name='Kharkiv')

Session = sessionmaker(bind=engine)
session = Session()
session.add(new_hotel)
session.commit()
