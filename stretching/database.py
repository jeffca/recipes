from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlite3

engine = create_engine('sqlite:///jess.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
	import stretching.models
	Base.metadata.create_all(bind=engine)

def reset_db():
	import stretching.models
	Base.metadata.drop_all(bind=engine)