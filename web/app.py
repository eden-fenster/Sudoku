#!/usr/bin/env python3
import logging
import sys
from typing import List
import web.sudoku
from flask import Flask, request, render_template, render_template_string
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
    # Gets the file and saves it.
    f = request.files['file']
    f.save(f.filename)
    # Reads the file, exit if it's an invalid file.
    read_file: List[str] = web.sudoku.read_file(file_to_open=f.filename)
    if not read_file:
        logging.error("No sudoku found")
        sys.exit(1)
    # Convert to a grid.
    initial_grid: List[List[int]] = web.sudoku.create_sudoku(read_file)
    # Delete previous records.
    requests.delete("http://sudoku_processor:8000/grids")
    # Send parameter to processor.
    requests.post("http://sudoku_processor:8000/grids", json={"Grid": initial_grid})
    get_response = requests.get("http://sudoku_processor:8000/grids")
    # Return response.
    response = get_response.json()
    return render_template('style.html') + render_template_string(response)


#
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='sudoku_web')
