#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect(f'sudoku_results.db')
c = conn.cursor()
command = f"""CREATE TABLE sudoku_results (
results text
)"""
c.execute(command)
conn.commit()
conn.close()
