# syntax=docker/dockerfile:1

FROM python:3.10.6

WORKDIR /query_directory


ENV FLASK_APP=query/app.py
ENV FLASK_RUN_HOST=0.0.0.0


COPY query/requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install inetutils-ping
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 1000

# Copy database to directory.
COPY query/*.py /query_directory/query/
COPY query/templates/*.html /query_directory/query/templates/
COPY query/static/styles/*.css /query_directory/query/static/styles/

CMD ["flask", "run", "-p", "1000"]