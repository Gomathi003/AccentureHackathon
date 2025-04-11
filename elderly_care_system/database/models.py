from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Elder(Base):
    __tablename__ = 'elders'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    emergency_contact = Column(String)
    medical_conditions = Column(String)
    
class HealthData(Base):
    __tablename__ = 'health_data'
    id = Column(Integer, primary_key=True)
    elder_id = Column(Integer)
    heart_rate = Column(Float)
    blood_pressure = Column(String)
    glucose_level = Column(Float)
    timestamp = Column(DateTime, default=datetime.now)
    
class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    elder_id = Column(Integer)
    activity_type = Column(String)
    location = Column(String)
    timestamp = Column(DateTime, default=datetime.now)

# Initialize database
engine = create_engine('sqlite:///elderly_care.db')
Base.metadata.create_all(engine)