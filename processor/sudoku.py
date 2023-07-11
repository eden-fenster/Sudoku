#!/usr/bin/env python3
"""Sudoku Solver - Relevant methods"""
import logging
from typing import List
from processor.new_sudoku_class import puzzle

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def print_grid(description: str, grid: List[List[int]]) -> str:
    """Printing grid"""
    logging.debug("Received grid")
    print(description)
    grid_string: str = ''
    for grid_line in grid:
        grid_line_converted = map(str, grid_line)
        grid_string += ' '.join(grid_line_converted) + "<br>"
        logging.debug('The grid so far is \n %s', grid_string)
    logging.debug("Grid converted to string")
    return grid_string


def get_solutions(initial_grid: List[List[int]]) -> List[List[int]]:
    """Getting solution"""
    logging.debug("Received solution")
    solutions = puzzle(grid=initial_grid)
    return solutions
