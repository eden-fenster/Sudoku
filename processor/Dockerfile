# syntax=docker/dockerfile:1

FROM python:3.10.6

WORKDIR /sudoku_processor

ENV FLASK_APP=processor/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .

CMD ["flask", "run"]