#!/usr/bin/env python3
"""Sudoku Solver - Query Database"""
import logging

import requests
from flask import Flask, render_template, render_template_string, request

app = Flask(__name__)


# return the database.
@app.route('/')
def home():
    """Get dates"""
    return render_template('dates.html')


# Putting a template for when the dates will be received.
@app.route('/queried', methods=['GET', 'POST'])
def return_queried():
    """Return queried"""
    # Getting dates.
    start_date = request.form.get('startdate')
    end_date = request.form.get('enddate')
    logging.debug("The start date is %s and the end date is %s", start_date, end_date)
    # Send to database.
    requests.post('http://sudoku_database:3000/queried', json={"Start": start_date, "End": end_date}, timeout=10)
    logging.debug("Sent")
    response = requests.get('http://sudoku_database:3000/queried', timeout=10)
    return render_template('results.html', Title='Queried Database') \
        + render_template_string(response.json())


if __name__ == '__main__':
    app.run(debug=True, port=1000, host='sudoku_query')