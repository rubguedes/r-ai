from sqlalchemy.orm import Session

from app.models.conversation import Conversation

from app.core.logger import logger


class ConversationRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, title: str):
        conversation = Conversation(title=title)
        logger.info(f"Creating conversation: {title}")

        self.db.add(conversation)
        self.db.commit()
        logger.info(f"Conversation created with ID: {conversation.id}")
        self.db.refresh(conversation)

        return conversation

    def list_all(self):
        logger.info("Listing conversations")
        return self.db.query(Conversation).all()
    
    def find_by_id(self, conversation_id: int):
        return (self.db.query(Conversation).filter(Conversation.id == conversation_id).first())
