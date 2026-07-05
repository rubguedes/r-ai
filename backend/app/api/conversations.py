from fastapi import APIRouter, Depends

from app.dependencies.service import get_conversation_service
from app.schemas.conversation import CreateConversationRequest
from app.schemas.message import SendMessageRequest
from app.services.conversation_service import ConversationService

router = APIRouter()


@router.get("/conversations")
def list_conversations(service: ConversationService = Depends(get_conversation_service)):
    return service.list_conversations()


@router.get("/conversations/{conversation_id}/messages")
def get_conversation_history(conversation_id: int, service: ConversationService = Depends(get_conversation_service)):
    return service.get_conversation_history(conversation_id)


@router.post("/conversations")
def create_conversation(request: CreateConversationRequest, service: ConversationService = Depends(get_conversation_service)):
    return service.create_conversation(request.title)


@router.post("/conversations/{conversation_id}/messages")
def send_message(conversation_id: int, request: SendMessageRequest, service: ConversationService = Depends(get_conversation_service)):
    return service.send_message(conversation_id, request.content)
