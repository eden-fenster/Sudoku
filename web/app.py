#!/usr/bin/env python3
import logging
import sys
from typing import List
from processor.app import GetResults


from flask import *

import sudoku

app = Flask( __name__)


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
        return GetResults.get(initial_grid=initial_grid)


if __name__ == '__main__':
    app.run(debug=True)
