#!/usr/bin/env python3
import json
import logging
import re
import subprocess

import requests

import processor.sudoku
from flask import Flask, request, render_template_string

app = Flask(__name__)

# List to store received grid.
grids = []
# List to store the returned results.
grid_strings = []



# Returns the results
@app.route('/grids')
def get_grids():
    # Turning grid into a string.
    results = json.dumps(grid_strings)
    formatted_grids = re.sub(r"[\[\]]", "", results)
    # Return results.
    return json.dumps(formatted_grids)


@app.route('/grids', methods=['POST'])
def add_grids():
    # Add grid to records.
    grids.append(request.get_json())
    initial_grid = grids[0]["Grid"]
    # Convert input to string.
    initial_string: str = processor.sudoku.print_grid(description="Initial grid", grid=initial_grid)
    # Solve the sudoku.
    solved = processor.sudoku.get_solutions(initial_grid=initial_grid)
    solved_string: str = ''
    for i, solve in enumerate(solved):
        solved_string += processor.sudoku.print_grid(description=f"solution {i + 1}", grid=solve)
    # Clears list from previous attempts
    grid_strings.clear()
    # Add to list.
    logging.debug(f"Adding {solved_string} to list")
    grid_strings.append("Initial Grid: <br>" + initial_string + "<br>Solved Grid: <br>" + solved_string)
    # Adding record to database
    requests.post("http://sudoku_database:3000/database", json={"Result": 'y'})
    logging.debug("Added to database")
    # Checking if we are the first record in the database, if yes, delete.
    requests.delete("http://sudoku_database:3000/database")
    return '', 204


# Delete previous records.
@app.route('/grids', methods=['DELETE'])
def delete_grids():
    grids.clear()
    grid_strings.clear()
    return '', 204


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='sudoku_processor')
