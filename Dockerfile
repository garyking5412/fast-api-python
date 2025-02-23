FROM ubuntu:latest
LABEL authors="minazuki"
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 9001
CMD ["uvicorn", "Python-beginner:app","--host", "0.0.0.0", "--port", "9001"]