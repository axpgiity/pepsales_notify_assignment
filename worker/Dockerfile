FROM python:3.11

WORKDIR /worker

COPY .. .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "worker/consumer.py"]
