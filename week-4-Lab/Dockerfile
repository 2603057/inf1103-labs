FROM python:3.11-slim

WORKDIR /app

COPY persistent_auditor.py .
COPY orders.txt .

CMD ["python", "persistent_auditor.py"]