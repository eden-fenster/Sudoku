#!/usr/bin/env bash

FILE=sudoku_results.db
if test -f "databases/$FILE"; then
    mv databases/$FILE /sudoku_database_directory
    chmod 775 $FILE
fi
