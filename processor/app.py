#!/usr/bin/env python3
from typing import List

from flask import *
from flask_restful import *

import sudoku

app = Flask(__name__)
api = Api(app)


def sudoku_solver(initial_grid: List[List[int]]):
    initial_grid_string = sudoku.print_grid(description="Initial grid", grid=initial_grid)
    solutions = sudoku.get_solutions(initial_grid=initial_grid)
    solved_grid_string: str = ''
    for i, solution in enumerate(solutions):
        solved_grid_string += sudoku.print_grid(description=f"solution {i + 1}", grid=solution)

    sudoku_json: str = 'The initial grid: <br>' + initial_grid_string + \
                       '<br>The solved grid: <br>' + solved_grid_string

    return json.dumps(sudoku_json)


class GetResults(Resource):
    def get(initial_grid: List[List[int]]):
        return_object: str = sudoku_solver(initial_grid=initial_grid)
        return make_response(return_object)


api.add_resource(GetResults, '/')

if __name__ == '__main__':
    app.run(debug=True)
