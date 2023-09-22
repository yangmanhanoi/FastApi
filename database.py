from sqlalchemy import create_engine
# Declare the mapping
from sqlalchemy.ext.declarative import declarative_base
# Create a session
from sqlalchemy.orm import sessionmaker
SQLALCHAMY_DATABASE = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHAMY_DATABASE, connect_args={"check_same_thread": False})

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)