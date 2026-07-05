from pydantic import BaseModel


class CreateConversationRequest(BaseModel):
    title: str


class ConversationResponse(BaseModel):
    id: int
    title: str

    model_config = {
        "from_attributes": True
    }