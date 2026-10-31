FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir django pymysql cryptography
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]