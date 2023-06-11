#!/usr/bin/env bash

FILE=sudoku_results.db
if test -f "$FILE"; then
    mv databases/FILE /sudoku_database_directory/database
    chmod 775 /sudoku_database_directory/database/FILE
fi
