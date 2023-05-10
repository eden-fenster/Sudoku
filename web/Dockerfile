# syntax=docker/dockerfile:1

FROM python:3.10.6

WORKDIR /sudoku_web

ENV FLASK_APP=web/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY web/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000


COPY web/*.py /sudoku_web/web/
COPY web/templates/*.html /sudoku_web/web/templates/


CMD ["flask", "run"]