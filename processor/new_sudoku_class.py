#!/usr/bin/env python3
"""Solving a Sudoku"""
import math
from typing import List


# pylint: disable=invalid-name
def solved_puzzle(grid: List[List[int]]) -> List[List[int]]:
    """Solving and returning a solved grid"""
    is_puzzle_legit(grid=grid, row=0, col=0)
    return grid


def solve_puzzle(grid: List[List[int]], row: int, col: int, num: int) -> bool:
    """Solving the sudoku for given number"""
    length: int = len(grid[0])
    square_length: int = int(math.sqrt(length))
    for x in range(length):
        # If number in row, false.
        if grid[row][x] == num:
            return False

    for x in range(length):
        # If number in col, false.
        if grid[x][col] == num:
            return False

    start_row = row - row % square_length
    start_col = col - col % square_length
    for i in range(square_length):
        for j in range(square_length):
            # If number in square, false.
            if grid[i + start_row][j + start_col] == num:
                return False
    # Else, true.
    return True


def is_puzzle_legit(grid: List[List[int]], row: int, col: int) -> bool:
    """Checking if sudoku is solvable"""
    length: int = len(grid[0])
    # If at end, return true
    if row == length - 1 and col == length:
        return True
    # If at end of row, move to next.
    if col == length:
        row += 1
        col = 0
    # If occupied, move to next square.
    if grid[row][col] > 0:
        return is_puzzle_legit(grid, row, col + 1)
    # Checking if solvable for each number.
    for num in range(1, length + 1, 1):

        if solve_puzzle(grid, row, col, num):
            # If solvable, put in number.
            grid[row][col] = num
            # If next square is solvable, return True.
            if is_puzzle_legit(grid, row, col + 1):
                return True
        # If not solvable for number, set to zero.
        grid[row][col] = 0
    # Else, return false.
    return False
