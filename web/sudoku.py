#!/usr/bin/env python3
"""Sudoku Solver - Relevant methods"""
import logging
from typing import List

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


# Reads in a file
def read_file(file_to_open: str) -> List[str]:
    """Reading the file"""
    list_of_lines: List[str] = []
    # Reading the file by line.
    try:
        with open(file_to_open, 'r', encoding='UTF-8') as file:
            for line in file.readlines():
                list_of_lines.append(line.rstrip())
    except OSError as exception:
        logging.error('Unable to open file %s: %s', file_to_open, exception)
        return []
    return list_of_lines


def create_sudoku_line(line: str) -> List[int]:
    """Creating sudoku line"""
    sudoku_line: List[int] = []
    for character in line:
        if character == ' ':
            continue
        if not character.isdigit():
            logging.warning('Found a non-numerical character %s in %s', character, line)
            continue
        sudoku_line.append(int(character))
    return sudoku_line


# Converts a file into a two-dimensional list.
def create_sudoku(list_of_lines: List[str]) -> List[List[int]]:
    """Creating the sudoku"""
    # Converting the lines into numbers, creating a two-dimensional list of ints.
    sudoku: List[List[int]] = []
    for line in list_of_lines:
        sudoku_line = create_sudoku_line(line=line)
        sudoku.append(sudoku_line)
    return sudoku
