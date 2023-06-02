#!/usr/bin/env python3
"""Sudoku Solver - Query Database"""
import requests
from flask import Flask, render_template, render_template_string

app = Flask(__name__)


# return the database.
@app.route('/')
def get_database():
    """Return our database"""
    response = requests.get('http://sudoku_database:3000/database', timeout=10)
    return render_template('results.html', Title='Database')\
        + render_template_string(response.json())


# Putting a template for when the dates will be received.
@app.route('/', methods=['POST'])
def post():
    """Get dates from user"""
    return '', 204

# TODO: Something similar to the interface in the web container.


if __name__ == '__main__':
    app.run(debug=True, port=1000, host='sudoku_query')
