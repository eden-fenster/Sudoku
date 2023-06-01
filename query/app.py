#!/usr/bin/env python3
"""Sudoku Solver - Query Database"""
import requests
from flask import Flask, render_template, render_template_string

app = Flask(__name__)


# return the database.
@app.route('/')
def get_database():
    """Return our database"""
    response = requests.get('http://sudoku_database:3000/database')
    return render_template('results.html', Title='Database') + render_template_string(response.json())

# TODO: Query database between dates.


if __name__ == '__main__':
    app.run(debug=True, port=1000, host='sudoku_query')
