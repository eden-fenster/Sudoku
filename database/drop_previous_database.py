#!/usr/bin/env python3
"""Deleting a database"""
import sqlite3

# pylint: disable=invalid-name


def create(database_name: str):
    """Deleting a database"""
    conn = sqlite3.connect(f'{database_name}.db', check_same_thread=False)
    c = conn.cursor()
    command = f"DROP TABLE IF EXISTS {database_name}"
    c.execute(command)
    conn.commit()
