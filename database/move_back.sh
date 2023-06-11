#!/usr/bin/env bash

FILE=/databases/sudoku_results.db
if test -f "$FILE"; then
    mv FILE /sudoku_database_directory/database
fi
