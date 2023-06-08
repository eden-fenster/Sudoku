#!/usr/bin/env python3
"""Sudoku Solver - Database"""
import json
import logging
import re
from datetime import datetime
from typing import List

from log_database import Database
from create_database import create
from flask import Flask, request

app = Flask(__name__)

# pylint: disable=invalid-name

# List to store received response.
responses: List[dict] = []
queried_dates: List[dict] = []
queried: List[str] = []
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
    date = datetime.strptime(responses[len(responses) - 1]["Date"], '%Y-%m-%d %H:%M')
    # Create database.
    create(database_name='sudoku_results')
    # Move database.
    # subprocess.call("./database/move.sh")
    logging.debug("created")
    # Adding to database
    sudoku_db.add_one(time=time, our_date=date)
    return '', 204


# Delete previous records.
@app.route('/database', methods=['DELETE'])
def delete_records(id_to_delete: str):
    """Deleting from database"""
    sudoku_db.delete_one(id=id_to_delete)
    logging.debug("record deleted")
    return '', 204


# Get between queried dates.
@app.route('/queried', methods=['POST'])
def post_queried():
    """Getting dates from user"""
    queried_dates.append(request.get_json())
    logging.debug("Received")
    start = queried_dates[len(queried_dates) - 1]["Start"]
    end = queried_dates[len(queried_dates) - 1]["End"]
    between_dates = sudoku_db.query_between_two_days(start_date=start, end_date=end)
    queried.clear()
    queried.append(between_dates)
    return '', 204


# Return between queried dates.
@app.route('/queried')
def get():
    """Returning the dates"""
    # Turning grid into a string.
    database = json.dumps(queried)
    formatted_database = re.sub(r"[\[\]]", "", database)
    # Return results.
    return json.dumps(formatted_database)


if __name__ == '__main__':
    app.run(debug=True, port=3000, host='sudoku_database')
