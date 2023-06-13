#!/usr/bin/env python3
"""Creating our database"""
import logging
from create_database import create


def created():
    """Creating our database"""
    create(database_name='sudoku_results')
    logging.debug("Created")
