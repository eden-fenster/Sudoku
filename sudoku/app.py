#!/usr/bin/env python3
import logging
import sys
from typing import List

from flask import *

import sudoku

app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/results', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        read_file: List[str] = sudoku.read_file(file_to_open=f.filename)
        if not read_file:
            logging.error(f"No sudoku found")
            sys.exit(1)
        initial_grid: List[List[int]] = sudoku.create_sudoku(read_file)
        initial_grid_string = sudoku.print_grid(description="Initial grid", grid=initial_grid)
        solutions = sudoku.get_solutions(initial_grid=initial_grid)
        solved_grid_string: str = ''
        for i, solution in enumerate(solutions):
            solved_grid_string += sudoku.print_grid(description=f"solution {i + 1}", grid=solution)

        sudoku_json: str = 'The initial grid: <br>' + initial_grid_string +\
                           '<br>The solved grid: <br>' + solved_grid_string

        return json.dumps(sudoku_json)
    return json.dumps({"Fail"})


if __name__ == '__main__':
    app.run(debug=True)
