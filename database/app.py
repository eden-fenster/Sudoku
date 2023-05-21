#!/usr/bin/env python3
import json
import logging
import re
import subprocess
from flask import Flask, request


app = Flask(__name__)

# List to store received response.
responses = []


# Returns the results
@app.route('/database')
def get_database():
    # TODO: return database contents in jSONfied way.
    pass


@app.route('/database', methods=['POST'])
def add_to_database():
    # TODO: Add to list.
    # TODO: Check if exists.
    # TODO: If not, create database.
    # TODO: Add to database.
    pass


# Delete previous records.
@app.route('/database', methods=['DELETE'])
def delete_records():
    # TODO: Delete previous records from database.
    pass


if __name__ == '__main__':
    app.run(debug=True, port=3000, host='sudoku_database')
