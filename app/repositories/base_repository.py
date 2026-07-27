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

    def update(self, entity: ModelType) -> ModelType:
        self.db.commit()
        self.db.refresh(entity)

        return entity

    def delete(self, entity: ModelType) -> None:
        self.db.delete(entity)
        self.db.commit()

    def get_by_id(self, entity_id: int) -> ModelType | None:

        statement = select(self.model).where(
            self.model.id == entity_id #type: ignore
        )

        return self.db.scalar(statement)


    def get_all(self) -> list[ModelType]:
        statement = select(self.model)
        return list(self.db.scalars(statement).all())