#!/usr/bin/env python3
"""Sudoku Solver - Query Database"""
import logging

import requests
from flask import Flask, render_template, render_template_string, request

app = Flask(__name__)


# return the database.
@app.route('/')
def get_database():
    """Return our database"""
    response = requests.get('http://sudoku_database:3000/database', timeout=10)
    return render_template('results.html', Title='Database')\
        + render_template_string(response.json())


# Putting a template for when the dates will be received.
@app.route('/queried', methods=['GET', 'POST'])
def post():
    """Get dates from user"""
    # Getting dates.
    start_date = request.form.get('startdate')
    end_date = request.form.get('enddate')
    logging.debug("The start date is %s and the end date is %s", start_date, end_date)
    return '', 204

# TODO: Have post send them in a RESTful way to database container.
# TODO: Have the database container get them and return between dates.


if __name__ == '__main__':
    app.run(debug=True, port=1000, host='sudoku_query')
