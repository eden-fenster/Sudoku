#!/usr/bin/env python3
from typing import List

from flask import *

import sudoku

sudoku_processor = Blueprint('sudoku_processor', __name__)



@sudoku_processor.route('/', methods=['GET', 'POST'])
def sudoku_solver(initial_grid: List[List[int]]):
    if request.method == 'POST':
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
