#!/usr/bin/env python3
"""Creating our database"""
import logging
from database.create_database import create


def created():
    """Creating our database"""
    create(directory='sudoku_database_directory/database', database_name='sudoku_results')
    logging.debug("Created")
