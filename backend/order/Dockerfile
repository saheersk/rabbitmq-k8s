FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y libpq-dev

WORKDIR /product-order

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .