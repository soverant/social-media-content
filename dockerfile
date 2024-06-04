FROM python:3.8-alpine

RUN pip install python-telegram-bot --upgrade

WORKDIR /app

add . ./

CMD python main.py