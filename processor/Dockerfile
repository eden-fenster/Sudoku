# syntax=docker/dockerfile:1

FROM python:3.10.6

WORKDIR /sudoku_processor_directory


ENV FLASK_APP=processor/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY processor/requirements.txt requirements.txt
RUN apt-get -y update
RUN apt-get install inetutils-ping
RUN apt-get -y install curl
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

# Copy database to directory.
COPY processor/*.py /sudoku_processor_directory/processor/


CMD ["flask", "run", "-p", "8000"]


