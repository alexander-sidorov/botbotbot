from typing import List
from typing import Optional

from pydantic import Field
from pydantic.main import BaseModel


class Chat(BaseModel):
    id: int
    type: str
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class User(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None


class MessageEntity(BaseModel):
    type: str
    offset: int
    length: int
    url: Optional[str] = None
    user: Optional[User] = None
    language: Optional[str] = None


class Message(BaseModel):
    message_id: int
    date: int
    chat: Chat
    from_: Optional[User] = None
    text: Optional[str] = None

    class Config:
        fields = {
            "from_": "from",
        }


class Update(BaseModel):
    update_id: int
    message: Optional[Message] = None


class WebhookInfo(BaseModel):
    url: str
    has_custom_certificate: bool
    pending_update_count: int
    allowed_updates: List[str] = Field(default_factory=list)
    ip_address: Optional[str] = None
    last_error_date: Optional[int] = None
    last_error_message: Optional[str] = None
    max_connections: Optional[int] = None


# ==== post setup =========================================

Message.update_forward_refs()
