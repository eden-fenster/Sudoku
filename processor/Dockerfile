# syntax=docker/dockerfile:1

FROM python:3.10.6

WORKDIR /sudoku_processor

ENV FLASK_APP=processor/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONPATH=.

COPY processor/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000


COPY processor/*.py /sudoku_processor/processor/

ENTRYPOINT python processor/app.py
# CMD ["flask", "run", "-p", "8000"]