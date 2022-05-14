import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)


class User(Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    height = Column(String(120), unique=True, nullable=False)
    mass = Column(String(120), unique=True, nullable=False)
    hair_color = Column(String(120), unique=True, nullable=False)
    skin_color = Column(String(120), unique=True, nullable=False)
    eye_color = Column(String(120), unique=True, nullable=False)
    birth_year = Column(String(120), unique=True, nullable=False)
    gender = Column(String(120), unique=True, nullable=False)

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    diamater = Column(String(120), unique=True, nullable=False)
    rotation_period = Column(String(120), unique=True, nullable=False)
    orbital_period = Column(String(120), unique=True, nullable=False)
    gravity = Column(String(120), unique=True, nullable=False)
    population = Column(String(120), unique=True, nullable=False)
    terrain = Column(String(120), unique=True, nullable=False)
    surface_water = Column(String(120), unique=True, nullable=False)
    
class Vehicles(Base):
    __tablename__ = 'Vehicles'
    id = Column(Integer, primary_key=True)
    model = Column(String(120), unique=True, nullable=False)
    vehicle_class = Column(String(120), unique=True, nullable=False)
    manufacturer = Column(String(120), unique=True, nullable=False)
    cost_in_credits = Column(String(120), unique=True, nullable=False)
    length = Column(String(120), unique=True, nullable=False)
    crew = Column(String(120), unique=True, nullable=False)
    passengers = Column(String(120), unique=True, nullable=False)
    max_atmostphering_speed = Column(String(120), unique=True, nullable=False)
    cargo_capacity = Column(String(120), unique=True, nullable=False)
    consumables = Column(String(120), unique=True, nullable=False)
    
    def to_dict(self):
        return {}




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')