# syntax=docker/dockerfile:1

FROM python:3.10.6

WORKDIR /sudoku_web_directory

ENV FLASK_APP=web/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY web/requirements.txt requirements.txt
RUN apt-get -y update
RUN apt-get install inetutils-ping
RUN apt-get -y install curl
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000


COPY web/*.py /sudoku_web_directory/web/
COPY web/templates/*.html /sudoku_web_directory/web/templates/
COPY web/static/styles/*.css /sudoku_web_directory/web/static/styles/
COPY web/static/scripts/*.js /sudoku_web_directory/web/static/scripts/
COPY web/static/*.ico /sudoku_web_directory/web/static/

CMD ["flask", "run"]