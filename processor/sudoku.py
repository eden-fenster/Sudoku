#!/usr/bin/env python3
"""Sudoku Solver - Relevant methods"""
import logging
from typing import List
from processor.sudoku_class import solve_sudoku

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def print_grid(description: str, grid: List[List[int]]) -> str:
    """Printing grid"""
    print(description)
    grid_string: str = ''
    for grid_line in grid:
        grid_line_converted = map(str, grid_line)
        grid_string += ' '.join(grid_line_converted) + "<br>"
        logging.debug('The grid so far is \n %s', grid_string)
    return grid_string


def get_solutions(initial_grid: List[List[int]]) -> List[List[int]]:
    """Getting solution"""
    solutions, have_solution, information = solve_sudoku(grid=initial_grid)
    _ = have_solution
    _ = information
    return solutions
