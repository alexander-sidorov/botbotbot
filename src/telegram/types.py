from typing import List
from typing import Optional

from pydantic import Field
from pydantic.main import BaseModel


class Chat(BaseModel):
    first_name: Optional[str] = Field(default=None)
    id: int = Field(...)
    last_name: Optional[str] = Field(default=None)
    type: str = Field(...)
    username: Optional[str] = Field(default=None)


class User(BaseModel):
    first_name: str = Field(...)
    id: int = Field(...)
    is_bot: bool = Field(...)
    last_name: Optional[str] = Field(default=None)
    username: Optional[str] = Field(default=None)


class MessageEntity(BaseModel):
    language: Optional[str] = Field(default=None)
    length: int = Field(...)
    offset: int = Field(...)
    type: str = Field(...)
    url: Optional[str] = Field(default=None)
    user: Optional[User] = Field(default=None)


class Message(BaseModel):
    chat: Chat = Field(...)
    date: int = Field(...)
    entities: List[MessageEntity] = Field(default_factory=list)
    from_: Optional[User] = Field(default=None)
    message_id: int = Field(...)
    text: Optional[str] = Field(default=None)

    class Config:
        fields = {
            "from_": "from",
        }


class Update(BaseModel):
    message: Optional[Message] = Field(default=None)
    update_id: int = Field(...)


class WebhookInfo(BaseModel):
    allowed_updates: List[str] = Field(default_factory=list)
    has_custom_certificate: bool = Field(...)
    ip_address: Optional[str] = Field(default=None)
    last_error_date: Optional[int] = Field(default=None)
    last_error_message: Optional[str] = Field(default=None)
    max_connections: Optional[int] = Field(default=None)
    pending_update_count: int = Field(...)
    url: str = Field(...)


# ==== post setup =========================================

Message.update_forward_refs()
