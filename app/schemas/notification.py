from pydantic import BaseModel
from typing import Literal

class NotificationCreate(BaseModel):
    user_id: int
    type: Literal["email", "sms", "inapp"]
    message: str