FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y
RUN apt install pip -y


WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir

COPY . /app/
