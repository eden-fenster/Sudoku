#!/usr/bin/env python3
# Gets from user a 9 x 9 board.
import logging
from typing import List, Tuple
from processor.sudoku_class import solve_sudoku

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)



def dump_grid(description: str, grid: List[List[int]]) -> None:
    print(description)
    for grid_line in grid:
        grid_line_converted = map(str, grid_line)
        print(' '.join(grid_line_converted))
    print("")

def print_grid(description: str, grid: List[List[int]]) -> str:
    print(description)
    grid_string: str = ''
    for grid_line in grid:
        grid_line_converted = map(str, grid_line)
        grid_string += ' '.join(grid_line_converted) + "\n"
        logging.debug(f"The grid so far is \n {grid_string}")
    return grid_string

def get_solutions(initial_grid: List[List[int]]) -> Tuple[List[List[int]]]:
    solutions, have_solution, information = solve_sudoku(grid=initial_grid)
    _ = have_solution
    _ = information
    return solutions


# Reads in a file
def read_file(file_to_open: str) -> List[str]:
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


# Converts a file into a two-dimensional list.
def create_sudoku(list_of_lines: List[str]) -> List[List[int]]:
    # Converting the lines into numbers, creating a two-dimensional list of ints.
    sudoku: List[List[int]] = []
    for line in list_of_lines:
        sudoku_line = create_sudoku_line(line=line)
        sudoku.append(sudoku_line)
    return sudoku

