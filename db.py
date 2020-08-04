import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(os.getenv('SQLALCHEMY_DATABASE_URI')))
session = scoped_session(Session)