#!/usr/bin/env python3
"""Sudoku Solver - Web"""
import logging
import sys
from typing import List
from flask import Flask, request, render_template, render_template_string
import requests
from web import sudoku
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


# create an instance of flask
app = Flask(__name__)


# For GET request to http://localhost:5000/
@app.route('/')
def upload_file():
    """Getting file from the user"""
    logging.debug("Displaying home page")
    return render_template('upload.html')


# For Post request to http://localhost:5000/results
@app.route('/results', methods=['GET', 'POST'])
def post():
    """Sending in to processor and receiving input"""
    # Gets the file and saves it.
    received_file = request.files['file']
    logging.debug(f"Received file {received_file}")
    # If empty, return.
    if received_file.filename == '':
        return render_template('results.html') + render_template_string("No Grid has been provided")
    received_file.save(received_file.filename)
    logging.debug("The file is %s", received_file)
    # Reads the file, exit if it's an invalid file.
    logging.debug(f"Sending file {received_file} to be opened")
    read_file: List[str] = sudoku.read_file(file_to_open=received_file.filename)
    if not read_file:
        logging.error("No sudoku found")
        sys.exit(1)
    # Convert to a grid.
    logging.debug(f"Sending formatted file {read_file} to be converted to a grid")
    initial_grid: List[List[int]] = sudoku.create_sudoku(read_file)
    # Delete previous records.
    logging.debug("Deleting previous records")
    requests.delete("http://sudoku_processor:8000/grids", timeout=10)
    # Send parameter to processor.
    grid_to_send: dict = {"Grid": initial_grid}
    logging.debug(f"Sending sudoku {grid_to_send} to processor")
    requests.post("http://sudoku_processor:8000/grids", json=grid_to_send, timeout=10)
    get_response = requests.get("http://sudoku_processor:8000/grids", timeout=10)
    # Return response.
    response = get_response.json()
    logging.debug(f"Getting and returning response {get_response} from processor")
    return render_template('results.html', Title='Results', Second='Here are the results')\
        + render_template_string(response)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='sudoku_web', ssl_context='adhoc')
