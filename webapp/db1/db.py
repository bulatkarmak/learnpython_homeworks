from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('postgres://ueudvtji:euETzxJUFJ0OUCEBimVW8bJKpWR8nSb7@hattie.db.elephantsql.com:5432/ueudvtji')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()