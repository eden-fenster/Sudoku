# syntax=docker/dockerfile:1

FROM python:3.10.6

WORKDIR /sudoku_processor


ENV FLASK_APP=processor/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# ADD processor/logs.py /
COPY processor/requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install inetutils-ping
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# VOLUME /path/to

EXPOSE 8000


COPY processor/*.py /sudoku_processor/processor/


# CMD [ "python3", "./logs.py" ]
CMD ["flask", "run", "-p", "8000"]
