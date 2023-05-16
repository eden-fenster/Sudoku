# syntax=docker/dockerfile:1

FROM python:3.10.6

WORKDIR /sudoku_processor


ENV FLASK_APP=processor/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY processor/logs.sh .
RUN chmod 755 logs.sh && ./logs.sh
COPY processor/requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install inetutils-ping
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000


COPY processor/*.py /sudoku_processor/processor/


CMD ["cat", "output.log"]
CMD ["flask", "run", "-p", "8000"]
