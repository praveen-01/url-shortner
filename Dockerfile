FROM python:latest
WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY src/ /app/

CMD python3 main.py
