#!/usr/bin/env python3
"""Database class"""
import sqlite3


class Database:
    """The Database"""
    def __init__(self, database_name: str):
        self._database_name = database_name
        self._connection = sqlite3.connect(f'{database_name}.db', check_same_thread=False)
        self._cursor = self._connection.cursor()

    def show_all(self):
        """Printing all records"""
        self._cursor.execute(f"SELECT rowid, * FROM {self._database_name}")
        items = self._cursor.fetchall()
        for item in items:
            print(item)

    def show_one(self):
        """Printing a record"""
        self._cursor.execute(f"SELECT rowid, * FROM {self._database_name}")
        item = self._cursor.fetchone()
        print(item)

    # Add a new record to the table
    def add_one(self, result: str):
        """Adding a record"""
        self._cursor.execute(f"INSERT INTO {self._database_name} VALUES (?)", result)
        self._connection.commit()
        self._connection.close()

    def delete_one(self, i_d: str):
        """Deleting a record"""
        self._cursor.execute(f"DELETE from {self._database_name} WHERE rowid = (?)", i_d)
        self._connection.commit()
        self._connection.close()
