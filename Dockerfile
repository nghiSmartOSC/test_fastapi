FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /code/

COPY ./ /code/

RUN pip install -r requirements.txt

EXPOSE 8000