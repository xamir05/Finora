from typing import Generic, TypeVar

from sqlalchemy.orm import Session

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