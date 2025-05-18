from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Notification Service with RabbitMQ")
app.include_router(router)