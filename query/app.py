#!/usr/bin/env python3
"""Sudoku Solver - Query Database"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def get():
    """Return somethings"""
    return "Hello World"
# # List to store received response.
# responses = []
#
#
#
# # Returns the results
# @app.route('/database')
# def get_database():
#     """Getting from database"""
#     return json.dumps(sudoku_db.show_all())
#
#
# @app.route('/database', methods=['POST'])
# def add_to_database():
#     """Adding to database"""
#     # Adding to list.
#     responses.append(request.get_json())
#     time = responses[len(responses) - 1]["Time"]
#     date = responses[len(responses) - 1]["Date"]
#     # Create database.
#     create(database_name='sudoku_results')
#     logging.debug("created")
#     # Adding to database
#     sudoku_db.add_one(time=time, date=date)
#     return '', 204
#
#
# # Delete previous records.
# @app.route('/database', methods=['DELETE'])
# def delete_records():
#     """Deleting from database"""
#     if len(responses) > 1:
#         sudoku_db.delete_one(id='1')
#         logging.debug("record deleted")
#     return '', 204


if __name__ == '__main__':
    app.run(debug=True, port=1000, host='sudoku_query')
