#!/usr/bin/env python3
import json
import logging
import sys
from typing import List
import web.sudoku
from flask import Flask, request, render_template
import requests


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
    read_file: List[str] = web.sudoku.read_file(file_to_open=f.filename)
    if not read_file:
        logging.error(f"No sudoku found")
        sys.exit(1)
    initial_grid: List[List[int]] = web.sudoku.create_sudoku(read_file)
    # Delete previous records.
    requests.delete("http://172.23.0.1:8000/grids")
    # Send parameter to processor.
    requests.post("http://172.23.0.1:8000/grids", json={"Grid": initial_grid})
    get_response = requests.get("http://172.23.0.1:8000/grids")
    return get_response.json()

#
if __name__ == '__main__':
    app.run(debug=True, port=5000)
