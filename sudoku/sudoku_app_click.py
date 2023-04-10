import logging
import sys
from typing import List

import click
from flask import Flask
import sudoku

app = Flask(__name__)


@app.route('/')
@app.cli.command("Welcome to the Sudoku Solver Server. \n Input a sudoku file to solve.")
@click.argument("file")
def solve_sudoku(file):
    file = file
    read_file: List[str] = soduku.read_file(file_to_open=file)
    if not read_file:
        logging.error(f"No sudoku found")
        sys.exit(1)
    initial_grid: List[List[int]] = soduku.create_sudoku(read_file)
    print(soduku.dump_grid(description="Initial grid", grid=initial_grid))
    solutions, have_solution, information = soduku.solve_sudoku(grid=initial_grid)
    for i, solution in enumerate(solutions):
        print(soduku.dump_grid(description=f"solution {i + 1}", grid=solution))
