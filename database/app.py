#!/usr/bin/env python3
import json
import logging
import re
import subprocess
from log_database import Database
from flask import Flask, request

app = Flask(__name__)

# List to store received response.
responses = []


# Returns the results
@app.route('/database')
def get_database():
    db = Database()
    return json.dumps(db.show_all())


@app.route('/database', methods=['POST'])
def add_to_database():
    # Adding to list.
    responses.append(request.get_json())
    to_add_to_database = responses[0]["Result"]
    # Create database.
    subprocess.call("./database/create.sh")
    logging.debug("created")
    db = Database()
    # Adding to database
    db.add_one(result=to_add_to_database)
    return '', 204


# Delete previous records.
@app.route('/database', methods=['DELETE'])
def delete_records():
    db = Database()
    if len(responses) == 2:
        db.delete_one(id='1')
        logging.debug("record deleted")
    return '', 204



if __name__ == '__main__':
    app.run(debug=True, port=3000, host='sudoku_database')
