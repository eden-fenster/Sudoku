import logging
import sys
from typing import List

from flask import Flask, request, render_template
from flask_restful import Resource, Api

import sudoku

# create an instance of flask
app = Flask(__name__)
# creating an API object
api = Api(app)

# For GET request to http://localhost:5000/
class GetFromUser(Resource):
    def get(self):
        return render_template('upload.html')
    def post(self):
        return {'data': 'posted'}

# For Post request to http://localhost:5000/results
class PrintResults(Resource):
    def post(self):
        f = request.files['file']
        f.save(f.filename)
        read_file: List[str] = sudoku.read_file(file_to_open=f.filename)
        if not read_file:
            logging.error(f"No sudoku found")
            sys.exit(1)
        initial_grid: List[List[int]] = sudoku.create_sudoku(read_file)
        initial_grid_string = sudoku.print_grid(description="Initial grid", grid=initial_grid)
        solutions, have_solution, information = sudoku.solve_sudoku(grid=initial_grid)
        solved_grid_string: str = ''
        for i, solution in enumerate(solutions):
            solved_grid_string += sudoku.print_grid(description=f"solution {i + 1}", grid=solution)

        dict_sudoku: dict = {{"The initial grid: <br>": initial_grid_string},
                           {"<br>The solved grid: <br>" + solved_grid_string}}
        return dict_sudoku



api.add_resource(GetFromUser, '/')
api.add_resource(PrintResults, '/results')

#
if __name__ == '__main__':
    app.run(debug=True)