#!/usr/bin/env python3
"""Sudoku Solver - Database"""
import json
import logging
from log_database import Database
from create_database import create
from flask import Flask, request

app = Flask(__name__)

# pylint: disable=invalid-name

# List to store received response.
responses = []
queried_dates = []
sudoku_db = Database(database_name='sudoku_results')


# Returns the results
@app.route('/database')
def get_database():
    """Getting from database"""
    return json.dumps(sudoku_db.show_all())


@app.route('/database', methods=['POST'])
def add_to_database():
    """Adding to database"""
    # Adding to list.
    responses.append(request.get_json())
    time = responses[len(responses) - 1]["Time"]
    date = responses[len(responses) - 1]["Date"]
    # Create database.
    create(database_name='sudoku_results')
    logging.debug("created")
    # Adding to database
    sudoku_db.add_one(time=time, date=date)
    return '', 204


# Delete previous records.
@app.route('/database', methods=['DELETE'])
def delete_records(id_to_delete: str):
    """Deleting from database"""
    sudoku_db.delete_one(id=id_to_delete)
    logging.debug("record deleted")
    return '', 204


# Get and Return between queried dates.
@app.route('/queried', methods=['GET', 'POST'])
def get_queried():
    return "Hello"


if __name__ == '__main__':
    app.run(debug=True, port=3000, host='sudoku_database')
