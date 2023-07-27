#!/usr/bin/env python3
"""Sudoku Solver - Relevant methods"""
import logging
from typing import List
from new_sudoku_class import solved_puzzle

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def print_grid(description: str, grid: List[List[int]]) -> str:
    """Printing grid"""
    logging.debug(f"Received grid {grid}")
    print(description)
    grid_string: str = ''
    for grid_line in grid:
        grid_line_converted = map(str, grid_line)
        grid_string += ' '.join(grid_line_converted) + "<br>"
        logging.debug('The grid so far is \n %s', grid_string)
    logging.debug(f"Grid {grid_string} converted to string")
    return grid_string


def get_sudoku_solutions(initial_grid: List[List[int]]) -> List[List[int]]:
    """Getting solution"""
    solutions = solved_puzzle(grid=initial_grid)
    logging.debug(f"Received solution {solutions}")
    return solutions
