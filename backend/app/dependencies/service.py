from sqlalchemy.orm import Session
from fastapi import Depends
from app.database.dependencies import get_db
from app.repositories.conversation_repository import ConversationRepository
from app.repositories.message_repository import MessageRepository
from app.services.conversation_service import ConversationService

from app.core.logger import logger

def get_conversation_service(db: Session = Depends(get_db)) -> ConversationService:
    logger.info("Creating ConversationService dependency")
    conversation_repository = ConversationRepository(db)
    message_repository = MessageRepository(db)

    return ConversationService(conversation_repository, message_repository)