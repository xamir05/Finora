from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATABASE_URL = "sqlite:///./finora.db"


class Base(DeclarativeBase):
    pass

engine = create_engine(
    DATABASE_URL, 
    echo=True,
)


SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,

)    