#!/usr/bin/env python3
"""Sudoku Solver - Processor"""
import json
import logging
import re
import time
from datetime import datetime

import requests
from flask import Flask, request
from processor import sudoku
from processor.processor_storage import Storage

# pylint: disable=consider-using-f-string

app = Flask(__name__)


# Storing our lists
grids_to_return: Storage = Storage()


# Returns the results
@app.route('/grids')
def get_grids():
    """Returning the results"""
    # Turning grid into a string.
    results = json.dumps(grids_to_return.grid_strings)
    formatted_grids = re.sub(r"[\[\]]", "", results)
    # Return results.
    return json.dumps(formatted_grids)


@app.route('/grids', methods=['POST'])
def add_grids():
    """Solving the sudoku"""
    # Add grid to records.
    grids_to_return.grids.append(request.get_json())
    logging.debug("Received")
    initial_grid = grids_to_return.grids[0]["Grid"]
    # Convert input to string.
    initial_string: str = sudoku.print_grid(description="Initial grid", grid=initial_grid)
    # Getting current date and time
    now = datetime.now()
    dt_string_for_print = now.strftime("%m/%d/%Y, %H:%M:%S")
    dt_string = now.strftime("%Y-%m-%d %H:%M")
    start = time.time()
    # Solve the sudoku.
    solved = sudoku.get_solutions(initial_grid=initial_grid)
    end = time.time()
    total_time = end - start
    solved_string: str = sudoku.print_grid(description="Solved grid", grid=solved)
    # Clears list from previous attempts
    grids_to_return.grid_strings.clear()
    # Add to list.
    logging.debug("Adding %s to list", solved_string)
    grids_to_return.grid_strings.append\
        ("Initial Grid: <br>" + initial_string + "<br>Solved Grid: <br>" + solved_string +
         "<br>Time taken to solve: <br>" + str("%.2f" % total_time) + " seconds<br>"
         + "<br>Current Time: <br>" +
         dt_string_for_print)
    # Adding record to database
    total_time_string: str = str("%.2f" % total_time)
    requests.post("http://sudoku_database:3000/database",
                  json={"Solution": "Initial Grid: <br>" + initial_string + "<br>Solved Grid: <br>" + solved_string,
                        "Time": total_time_string, "Date": dt_string}, timeout=10)
    logging.debug("Added to database")
    return '', 204


# Delete previous records.
@app.route('/grids', methods=['DELETE'])
def delete_grids():
    """Deleting old grids"""
    grids_to_return.grids.clear()
    grids_to_return.grid_strings.clear()
    return '', 204


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='sudoku_processor')
