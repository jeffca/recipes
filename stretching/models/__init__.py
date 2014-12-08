from sqlalchemy import Column, Integer, String, Table, ForeignKey, DateTime, Boolean, Text, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy
from stretching.database import Base

class Muscle(Base):
	__tablename__ = 'Muscle'
	id = Column(Integer, primary_key=True)
	name = Column(String(50))

class Muscle_Pose(Base):
	__tablename__ = "Muscle_Pose"
	id = Column(Integer, primary_key=True)
	muscle_id = Column(Integer, ForeignKey("Muscle.id"))
	muscle = relationship("Muscle", backref="Muscle_Pose")
	pose_id = Column(Integer, ForeignKey("Pose.id"))
	pose = relationship("Pose", backref="Muscle_Pose")

class Pose(Base):
	__tablename__ = 'Pose'
	id = Column(Integer, primary_key=True)
	name = Column(String(50))
	description = Column(String(1200))
	img1url = Column(String(300))
	img2url = Column(String(300))
	classification_id = Column(Integer, ForeignKey("Classification.id"))
	classification = relationship("Classification", backref="Pose")

# class Pose_Classification

class Classification(Base):
	__tablename__ = 'Classification'
	id = Column(Integer, primary_key=True)
	name = Column(String(50))
