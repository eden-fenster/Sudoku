#!/usr/bin/env python3
"""Database class"""
import sqlite3


class Database:
    """The Database"""
    def __init__(self):
        self._connection = sqlite3.connect('sudoku_results.db')
        self._cursor = self._connection.cursor()

    def show_all(self):
        """Printing all records"""
        self._cursor.execute("SELECT rowid, * FROM sudoku_results")
        items = self._cursor.fetchall()
        for item in items:
            print(item)

    def show_one(self):
        """Printing a record"""
        self._cursor.execute("SELECT rowid, * FROM sudoku_results")
        item = self._cursor.fetchone()
        print(item)

    # Add a new record to the table
    def add_one(self, result: str):
        """Adding a record"""
        self._cursor.execute("INSERT INTO sudoku_results VALUES (?)", result)
        self._connection.commit()
        self._connection.close()

    def delete_one(self, i_d: str):
        """Deleting a record"""
        self._cursor.execute("DELETE from sudoku_results WHERE rowid = (?)", i_d)
        self._connection.commit()
        self._connection.close()
