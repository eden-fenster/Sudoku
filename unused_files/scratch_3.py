#!/usr/bin/env python3
import json
import logging
import sys
from typing import List, Tuple

from flask import Flask, request, render_template, jsonify
from flask_restful import Resource, Api
from processor.app import GetResults

import not_for_containers

# create an instance of flask
app = Flask(__name__)
# creating an API object
api = Api(app)


# For GET request to http://localhost:5000/
@app.route('/')
def upload_file():
    return render_template('upload.html')



# For Post request to http://localhost:5000/results
class PrintResults(Resource):
    def post(self):
        f = request.files['file']
        f.save(f.filename)
        read_file: List[str] = not_for_containers.read_file(file_to_open=f.filename)
        if not read_file:
            logging.error(f"No sudoku found")
            sys.exit(1)
        initial_grid: List[List[int]] = not_for_containers.create_sudoku(read_file)
        return GetResults.get(initial_grid=initial_grid)



api.add_resource(upload_file, '/')
api.add_resource(PrintResults, '/results')

#
if __name__ == '__main__':
    app.run(debug=True)
