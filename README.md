# Notification Service (Email, SMS, In-App) — with RabbitMQ & FastAPI

 a production-grade notification service built with FastAPI and RabbitMQ that supports:

 Email notifications  
 SMS notifications  
 In-app notifications  

A background worker consumes messages from RabbitMQ and processes them with retry support.

---

##  Features

- FastAPI backend with REST endpoints  
- Background worker using RabbitMQ (via Pika)  
- Retry logic for failed messages  
- Dockerized setup (API + RabbitMQ + Worker)  

---

##  Tech Stack

- FastAPI (Python)  
- RabbitMQ (Message Queue)  
- Docker + Docker Compose  

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/notification_service_rabbitmq.git
cd notification_service_rabbitmq
```

### 2. Build and start the services

```bash
docker-compose up --build
```

- **FastAPI app** at `http://localhost:8000`
- **RabbitMQ Management UI** at `http://localhost:15672`

  - Username: `guest`  
  - Password: `guest`

---

## 🧪 API Endpoints

### ➤ Send Notification

**POST** `/notifications`

```json
{
  "user_id": 1,
  "type": "email",        // or "sms" or "in-app"
  "message": "Hello from the Notification Service!"
}
```

### ➤ Get All Notifications for a User

**GET** `/users/{user_id}/notifications`

---

## 🛠 Retry Logic

Failed messages will be retried automatically using a basic backoff strategy. Retry attempts are logged in the worker logs.

---

## 🐇 RabbitMQ Dashboard

- **URL**: `http://localhost:15672`  
- **Login**: `guest` / `guest`

You can inspect queues, bindings, and message history here.

---

## Assumptions

- All notification types are logged instead of actually sending real emails/SMS.
- SQLite is used for demonstration; you can plug in PostgreSQL or MongoDB easily.
- This project is structured to easily extend with Celery, Redis, or Kafka.

---

## 📫 Contact

Created with  by Akshansh Pandey  
LinkedIn: [https://www.linkedin.com/in/akshansh-pandey-0380941ba/](https://www.linkedin.com/in/akshansh-pandey-0380941ba/)

---