FROM python:latest

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install flower

COPY . .