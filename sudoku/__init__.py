import logging
from typing import List


def read_file(file_to_open):
    list_of_lines: List[str] = []
    # Reading the file by line.
    try:
        with open(file_to_open, 'r', encoding='UTF-8') as file:
            for line in file.readlines():
                list_of_lines.append(line.rstrip())
    except OSError as exception:
        logging.error(f"Unable to open file {file_to_open}: {exception}")
        return []
    return list_of_lines


def create_sudoku(list_of_lines):
    # Converting the lines into numbers, creating a two-dimensional list of ints.
    sudoku: List[List[int]] = []
    for line in list_of_lines:
        sudoku_line = create_sudoku_line(line=line)
        sudoku.append(sudoku_line)
    return sudoku

def create_sudoku_line(line: str) -> List[int]:
    sudoku_line: List[int] = []
    for character in line:
        if character == ' ':
            continue
        if not character.isdigit():
            logging.warning(f"Found a non-numerical character '{character}' in {line}")
            continue
        sudoku_line.append(int(character))
    return sudoku_line