from app.database.connection import engine
from app.database.base import Base

from app.models.message import Message
from app.models.conversation import Conversation

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")