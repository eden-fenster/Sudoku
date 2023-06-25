# syntax=docker/dockerfile:1

FROM python:3.10.6

WORKDIR /sudoku_database_directory

ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0


COPY database/requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install inetutils-ping
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 3000

WORKDIR ../app
# Copy database to directory.
COPY database/app.py /sudoku_database_directory/app/app.py
COPY database/log_database.py /sudoku_database_directory/app/log_database.py

CMD ["cd.."]

WORKDIR ../database
COPY database/move.sh /sudoku_database_directory/database/move.sh
COPY database/create_database.py /sudoku_database_directory/database/create_database.py
COPY database/create_sudoku_results.py /sudoku_database_directory/database/create_sudoku_results.py

CMD ["cd.."]

WORKDIR /sudoku_database_directory

CMD ["flask", "run", "-p", "3000"]