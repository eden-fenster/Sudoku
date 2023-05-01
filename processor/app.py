#!/usr/bin/env python3
import json

from flask import Flask, jsonify, request
import sudoku
app = Flask(__name__)

# Initial grid string will be done in web.
grids = []
grid_strings = []


@app.route('/grids')
def get_grids():
    return json.dumps(grid_strings)


@app.route('/grids', methods=['POST'])
def add_grids():
    grids.append(request.get_json())
    initial_grid = grids[0]["Grid"]
    initial_string: str = sudoku.print_grid(description="Initial grid", grid=initial_grid)
    solved = sudoku.get_solutions(initial_grid=initial_grid)
    solved_string: str = ''
    for i, solve in enumerate(solved):
        solved_string += sudoku.print_grid(description=f"solution {i + 1}", grid=solve)
    grid_strings.append("Initial Grid: <br>" + initial_string + "<br>Solved Grid: <br>" + solved_string)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, port=8000)