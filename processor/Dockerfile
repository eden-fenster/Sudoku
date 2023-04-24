# syntax=docker/dockerfile:1

FROM python:3.10.6

WORKDIR /sudoku_processor

ENV FLASK_APP=app2.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run"]