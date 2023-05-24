#!/usr/bin/env python3
"""Creating a database"""
import sqlite3

conn = sqlite3.connect('sudoku_results.db')
c = conn.cursor()
command = """CREATE TABLE IF NOT EXISTS sudoku_results (
results text
)"""
c.execute(command)
conn.commit()
conn.close()
