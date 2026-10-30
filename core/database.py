from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

DATABASE_URL = "postgresql://username:password@localhost:5432/database_name"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    Base.metadata.create_all(bind=engine)


# autocommit=False----> Insert----> commit()
# autocommit=True----> Insert----> X


# autoflush=True
"""
NewData01
1.Insert 
2.Select
Fina Result NewData01
"""

# autoflush=False
"""
NewData01
1.Insert 
2.Select
Fina Result ()
"""    