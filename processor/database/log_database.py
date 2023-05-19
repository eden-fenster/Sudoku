#!/usr/bin/env python3
import sqlite3


class Database:
    def __init__(self):
        self._connection = sqlite3.connect('sudoku_results.db')
        self._cursor = self._connection.cursor()
        pass

    def show_all(self):
        self._cursor.execute("SELECT rowid, * FROM sudoku_results")
        items = self._cursor.fetchall()
        for item in items:
            print(item)

    # Add a new record to the table
    def add_one(self, result: str):
        self._cursor.execute("INSERT INTO sudoku_results VALUES (?, ?, ?)", result)
        self._connection.commit()
        self._connection.close()
