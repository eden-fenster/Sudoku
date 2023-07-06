#!/usr/bin/env python3
"""Sudoku Solver - Database"""
import json
import logging
import re

from datetime import datetime
from storage import Storage

from flask import Flask, request

app = Flask(__name__)

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
# pylint: disable=invalid-name

# A class with all of our things
sudoku: Storage = Storage(directory='database', database_name='sudoku_results')


# Returns the results
@app.route('/database')
def get_database():
    """Getting from database"""
    return json.dumps(sudoku.get_database().show_all())


@app.route('/database', methods=['POST'])
def add_to_database():
    """Adding to database"""
    # Adding to list.
    sudoku.get_responses().append(request.get_json())
    solution = sudoku.get_responses()[len(sudoku.get_responses()) - 1]["Solution"]
    time = sudoku.get_responses()[len(sudoku.get_responses()) - 1]["Time"]
    date = datetime.strptime(sudoku.get_responses()[len(sudoku.get_responses()) - 1]["Date"], '%Y-%m-%d %H:%M')
    # Adding to database
    logging.debug("Solution -> %s \n Time -> %s \n Date -> %s", solution, time, date)
    sudoku.get_database().add_one(solution=solution, time=time, our_date=date)
    return '', 204


# Delete previous records.
@app.route('/database', methods=['DELETE'])
def delete_records(id_to_delete: str):
    """Deleting from database"""
    sudoku.get_database().delete_one(id=id_to_delete)
    logging.debug("record deleted")
    return '', 204


# Get between queried dates.
@app.route('/queried', methods=['POST'])
def post_queried():
    """Getting dates from user"""
    sudoku.get_queried_dates().append(request.get_json())
    logging.debug("Received")
    start = sudoku.get_queried_dates()[len(sudoku.get_queried_dates()) - 1]["Start"]
    end = sudoku.get_queried_dates()[len(sudoku.get_queried_dates()) - 1]["End"]
    between_dates = sudoku.get_database().query_between_two_days(start_date=start, end_date=end)
    sudoku.get_queried().clear()
    sudoku.get_queried().append(between_dates)
    return '', 204


# Return between queried dates.
@app.route('/queried')
def get():
    """Returning the dates"""
    # Turning grid into a string.
    database = json.dumps(sudoku.get_queried())
    formatted_database = re.sub(r"[\[\]]", "", database)
    # Return results.
    return json.dumps(formatted_database)


if __name__ == '__main__':
    app.run(debug=True, port=3000, host='sudoku_database')
