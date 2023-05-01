#!/usr/bin/env python3
import logging
from typing import List

from flask import *
from flask_restful import *

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
import processor.sudoku

app = Flask(__name__)

# For Post request to http://localhost:8000
@app.route('/print', methods = ['GET', 'POST'])
def sudoku_solver():
    # TODO: Issue with receiving parameter from web.
    # TODO: Issue with connecting to localhost:8000
    input_json = request.get_json(force=True)
    logging.debug(f"The initial grid {input_json}")
    initial_grid_string = processor.sudoku.print_grid(description="Initial grid", grid=input_json)
    logging.debug(f"The initial grid string{initial_grid_string}")
    solutions = processor.sudoku.get_solutions(initial_grid=input_json)
    logging.debug(f"The solution {solutions}")
    solved_grid_string: str = ''
    for i, solution in enumerate(solutions):
        solved_grid_string += processor.sudoku.print_grid(description=f"solution {i + 1}", grid=solution)
    logging.debug(f"Solved grid {solved_grid_string}")
    sudoku_json: str = 'The initial grid: <br>' + initial_grid_string + \
                       '<br>The solved grid: <br>' + solved_grid_string

    return jsonify(sudoku_json)


if __name__ == '__main__':
    app.run(debug=True)