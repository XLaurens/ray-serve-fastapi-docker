FROM python:3.10-slim

ENV CONFIG_FILE_NAME=config.yaml

WORKDIR /app

COPY app.py  .
COPY config.yaml .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD  ["sh", "-c", "ray start --head --port=6379 --object-manager-port=8076 --include-dashboard=False && serve run $CONFIG_FILE_NAME"]
