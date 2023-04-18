# syntax=docker/dockerfile:1

# Enviorment
FROM python:3.10.6

# Directory
WORKDIR /sudoku_server

# Copying all files.
COPY . .

# Defining app and host.
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Installing dependencies.
RUN pip install --no-cache-dir  -r requirements-prod.txt

# Exposing port.
EXPOSE 5000

# Run.
CMD ["flask", "run"]
