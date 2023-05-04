# syntax=docker/dockerfile:1

FROM python:3.10.6

WORKDIR /sudoku_web

ENV FLASK_APP=web/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY web/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

COPY web/app.py .
COPY web/sudoku.py .
COPY web/sudoku_class.py .

CMD ["flask", "run"]