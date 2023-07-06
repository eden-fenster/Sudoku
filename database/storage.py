#!/usr/bin/env python3
"""Database storage object"""
import logging
import sys
from typing import List
from log_database import Database

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class Storage:
    def __init__(self, directory: str, database_name: str):
        """Creating storage for database and JSON lists that will be returned"""
        # Creating the database.
        sys.path.append(f"/sudoku_database_directory/{directory}/")
        from create_database import create
        create(directory=f'{directory}', database_name=f'{database_name}')
        logging.debug("created")
        # Variables.
        self._responses: List[dict] = []
        self._queried_dates: List[dict] = []
        self._queried: List[str] = []
        self._db = Database(directory=f'{directory}', database_name=f'{database_name}')

    def get_responses(self) -> List[dict]:
        """Return responses"""
        return self._responses

    def get_queried_dates(self) -> List[dict]:
        """Return dates to query"""
        return self._queried_dates

    def get_queried(self) -> List[dict]:
        """Return queried dates"""
        return self._queried

    def get_database(self):
        """Return database"""
        return self._db
