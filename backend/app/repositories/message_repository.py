from sqlalchemy.orm import Session

from app.models.message import Message

from app.core.logger import logger


class MessageRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, conversation_id: int, role: str, content: str):
        message = Message(conversation_id=conversation_id, role=role, content=content)
        logger.info(f"Creating message for conversation_id: {conversation_id}")

        self.db.add(message)
        self.db.commit()
        logger.info(f"Message created with id: {message.id}")
        self.db.refresh(message)

        return message

    def list_by_conversation(self, conversation_id: int):
        logger.info(f"Listing messages for conversation_id: {conversation_id}")
        return (
            self.db.query(Message)
            .filter(Message.conversation_id == conversation_id)
            .all()
        )
