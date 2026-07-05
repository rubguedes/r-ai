from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.models.base_entity import BaseEntity


class Conversation(Base, BaseEntity):
    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    # created_at: Mapped[str] = mapped_column(String(255))
