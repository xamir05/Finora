from app.database.database import Base, engine

from app.models.transaction import Transaction

def init_database():
    Base.metadata.create_all(bind=engine)