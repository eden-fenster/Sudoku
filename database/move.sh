#!/usr/bin/env bash

# Moving output and database to different volume
chmod +rw ./sudoku_results.db
mv sudoku_results.db /files
