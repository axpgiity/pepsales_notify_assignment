from fastapi import APIRouter
from app.schemas.notification import NotificationCreate
from app.queues.publisher import publish_notification

router = APIRouter()

@router.post("/notifications")
async def create_notification(notification: NotificationCreate):
    publish_notification(notification)
    return {"status": "queued"}

@router.get("/users/{user_id}/notifications")
async def get_notifications(user_id: int):
    from app.utils.database import notifications_db
    return [n for n in notifications_db if n["user_id"] == user_id]