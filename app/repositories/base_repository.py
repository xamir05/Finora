from typing import Generic, TypeVar

from sqlalchemy.orm import Session

from sqlalchemy import select

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):

    def __init__(self, db: Session, model: type[ModelType]):
        self.db = db
        self.model = model

    def create(self, entity: ModelType) -> ModelType:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)

        return entity

    def get_all(self) -> list[ModelType]:
        statement = select(self.model)
        return list(self.db.scalars(statement).all())