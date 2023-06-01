# syntax=docker/dockerfile:1

FROM python:3.10.6

WORKDIR /query_database_directory


ENV FLASK_APP=query_database/app.py
ENV FLASK_RUN_HOST=0.0.0.0


COPY query_database/requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install inetutils-ping
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 1000

# Copy database to directory.
COPY database/*.py /query_database_directory/database/

CMD ["flask", "run", "-p", "1000"]