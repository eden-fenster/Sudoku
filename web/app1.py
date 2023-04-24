#!/usr/bin/env python3
import logging
import sys
from typing import List
from processor import app2


from flask import *

import sudoku

sudoku_server = Flask( __name__)


@sudoku_server.route('/')
def upload_file():
    return render_template('upload.html')


@sudoku_server.route('/results', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        read_file: List[str] = sudoku.read_file(file_to_open=f.filename)
        if not read_file:
            logging.error(f"No sudoku found")
            sys.exit(1)
        initial_grid: List[List[int]] = sudoku.create_sudoku(read_file)
        return app2.sudoku_slover(initial_grid=initial_grid)


if __name__ == '__main__':
    sudoku_server.run(debug=True)
