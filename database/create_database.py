#!/usr/bin/env python3
"""Creating a database"""
import sqlite3

conn = sqlite3.connect('sudoku_results.db')
c = conn.cursor()
COMMAND = """CREATE TABLE IF NOT EXISTS sudoku_results (
results text
)"""
c.execute(COMMAND)
conn.commit()
conn.close()
