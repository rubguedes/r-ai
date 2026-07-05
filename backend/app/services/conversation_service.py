from app.repositories.conversation_repository import ConversationRepository
from app.exceptions.app_exceptions import NotFoundException

from app.core.logger import logger


class ConversationService:

    def __init__(self, repository: ConversationRepository, message_repository):
        self.repository = repository
        self.message = message_repository

    def create_conversation(self, title: str):
        logger.info(f"Creating conversation from service")
        return self.repository.create(title)

    def list_conversations(self):
        return self.repository.list_all()

    def send_message(self, conversation_id: int, content: str):
        logger.info(f"Processing message for conversation ID: {conversation_id}")
        self._get_conversation_or_raise(conversation_id)
        
        self.message.create(conversation_id, role="user", content=content)

        assistant_response = self._generate_response(content)

        self.message.create(
            conversation_id, role="assistant", content=assistant_response
        )

        return {
            "conversation_id": conversation_id,
            "assistant_response": assistant_response,
        }

    def get_conversation_history(self, conversation_id: int):
        return self.message.list_by_conversation(conversation_id)

    def _generate_response(self, message: str) -> str:
        logger.info("Generating assistant response")
        return f"You said: {message}"
    
    def _get_conversation_or_raise(self, conversation_id: int):
        conversation = self.repository.find_by_id(conversation_id)

        if conversation is None:
            raise NotFoundException("Conversation not found.")
        
        return conversation
