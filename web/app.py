#!/usr/bin/env python3
import json
import logging
import sys
from typing import List

from flask import Flask, request, render_template
import requests

import sudoku

# create an instance of flask
app = Flask(__name__)


# For GET request to http://localhost:5000/
@app.route('/')
def upload_file():
    return render_template('upload.html')



# For Post request to http://localhost:5000/results
@app.route('/results', methods=['GET', 'POST'])
def post():
    f = request.files['file']
    f.save(f.filename)
    read_file: List[str] = sudoku.read_file(file_to_open=f.filename)
    if not read_file:
        logging.error(f"No sudoku found")
        sys.exit(1)
    initial_grid: List[List[int]] = sudoku.create_sudoku(read_file)
    # Send parameter to processor.
    requests.post("http://localhost:8000/grids", json={"Grid": initial_grid})
    get_response = requests.get("http://localhost:8000/grids")
    return get_response.json()

#
if __name__ == '__main__':
    app.run(debug=True, port=5000)
