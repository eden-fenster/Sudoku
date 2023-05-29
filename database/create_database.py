#!/usr/bin/env python3
"""Creating a database"""
import sqlite3

# pylint: disable=invalid-name


def create(database_name: str):
    """Creating a database"""
    conn = sqlite3.connect(f'{database_name}.db', check_same_thread=False)
    c = conn.cursor()
    command = f"""CREATE TABLE IF NOT EXISTS {database_name} (
    results text,
    time real,
    date text
    )"""
    c.execute(command)
    conn.commit()
