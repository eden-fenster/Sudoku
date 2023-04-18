# syntax=docker/dockerfile:1

# Pull base image
FROM python:3.10.6-slim

# Get some custom packages
RUN apt-get update && apt-get install -y \
    build-essential \
    make \
    gcc \
    python3-dev \
    mongodb

## make local directory \
RUN mkdir /sudoku-api

# set as working directory
WORKDIR /sudoku-api

# copy files to /code
ADD . .

# pip install requirements
RUN pip install -r requirements-prod.txt

# Listen to port 5000
EXPOSE 5000

# start
CMD python manage.py runserver