FROM python:3.7-alpine
COPY service.py /app/
WORKDIR /app
CMD ["python3","service.py"]
