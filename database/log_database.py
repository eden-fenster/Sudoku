#!/usr/bin/env python3
"""Database class"""
import sqlite3


# pylint: disable=invalid-name
# pylint: disable=redefined-builtin

class Database:
    """The Database"""

    def __init__(self, database_name: str):
        self._database_name = database_name
        self._connection = sqlite3.connect(f'{database_name}.db', check_same_thread=False)
        self._cursor = self._connection.cursor()

    def show_all(self) -> str:
        """Printing all records"""
        self._cursor.execute(f"SELECT rowid, * FROM {self._database_name}")
        items = self._cursor.fetchall()
        items_string: str = ''
        for item in items:
            items_string += str(item) + "<br>"
        return items_string

    def show_one(self) -> str:
        """Printing a record"""
        self._cursor.execute(f"SELECT rowid, * FROM {self._database_name}")
        item = self._cursor.fetchone()
        return str(item)

    # Add a new record to the table
    def add_one(self, time: str, date: str):
        """Adding a record"""
        self._cursor.execute \
            (f"INSERT INTO {self._database_name} VALUES (?, ?)", (time, date))
        self._connection.commit()

    def delete_one(self, id: str):
        """Deleting a record"""
        self._cursor.execute(f"DELETE from {self._database_name} WHERE rowid = (?)", id)
        self._connection.commit()

    def query_between_two_days(self, start_date: str, end_date: str) -> str:
        """Showing records between two dates"""
        self._cursor.execute\
            (f"SELECT * FROM {self._database_name}"
             f" WHERE strftime('%Y-%m-%d', date) BETWEEN {start_date} AND {end_date}")
        items = self._cursor.fetchall()
        items_string: str = ''
        for item in items:
            items_string += str(item) + "<br>"
        return items_string
