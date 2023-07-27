#!/usr/bin/env python3
"""Sudoku Solver - Processor"""
import json
import logging
import re
import time
from datetime import datetime
from typing import List

import requests
from flask import Flask, request
import sudoku
from processor_storage import Storage

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

DATABASE_SERVER: str = "sudoku_database"
DATABASE_PORT: str = "3000"

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
    logging.debug(f"formatting the grid {results}")
    formatted_grids = re.sub(r"[\[\]]", "", results)
    # Return results.
    return json.dumps(formatted_grids)


@app.route('/grids', methods=['POST'])
def add_grids():
    """Solving the sudoku"""
    # Add grid to records.
    grids_to_return.grids.append(request.get_json())
    if not isinstance(grids_to_return.grids[len(grids_to_return.grids) - 1]["Grid"], List):
        our_object = grids_to_return.grids[len(grids_to_return.grids) - 1]["Grid"]
        raise TypeError(f"Grid is of invalid type {type(our_object)}")
    logging.debug(f"Received the grid {grids_to_return.grids[len(grids_to_return.grids) - 1]}")
    initial_grid = grids_to_return.grids[len(grids_to_return.grids) - 1]["Grid"]
    # Convert input to string.
    logging.debug(f"Sending grid {initial_grid} to be formatted to string")
    initial_string: str = sudoku.print_grid(description="Initial grid", grid=initial_grid)
    # Getting current date and time
    logging.debug("Getting current date and time")
    current_time = datetime.now()
    time_string_for_print = current_time.strftime("%m/%d/%Y, %H:%M:%S")
    time_string = current_time.strftime("%Y-%m-%d %H:%M")
    start_time = time.time()
    # Solve the sudoku.
    solved = sudoku.get_sudoku_solutions(initial_grid=initial_grid)
    logging.debug(f"solved sudoku {solved}")
    end_time = time.time()
    total_time = end_time - start_time
    logging.debug(f"Sending sudoku {solved} to be formatted to print")
    solved_string: str = sudoku.print_grid(description="Solved grid", grid=solved)
    # Clears list from previous attempts
    logging.debug(f"Clearing list {grids_to_return.grid_strings} from previous attempts")
    grids_to_return.grid_strings.clear()
    # Add to list.
    logging.debug("Adding %s to returned list", solved_string)
    grids_to_return.grid_strings.append \
        ("Initial Grid: <br>" + initial_string + "<br>Solved Grid: <br>" + solved_string +
         "<br>Time taken to solve: <br>" + str("%.2f" % total_time) + " seconds<br>"
         + "<br>Current Time: <br>" +
         time_string_for_print)
    # Adding record to database
    total_time_string: str = str("%.2f" % total_time)
    database_record: dict = {"Solution": "Initial Grid: <br>" + initial_string +
                                         "<br>Solved Grid: <br>" + solved_string,
                             "Time": total_time_string, "Date": time_string}
    requests.post(f"http://{DATABASE_SERVER}:{DATABASE_PORT}/database",
                  json=database_record, timeout=10)
    logging.debug(f"Added record {database_record} to database")
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
