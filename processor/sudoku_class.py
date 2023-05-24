#!/usr/bin/env python3
"""A class that helps us solve a sudoku"""
import math
from copy import deepcopy
from typing import List, Tuple, Set, Dict


# Not my code, from the internet, incorporating this into my program.
# pylint: disable=too-many-locals
# pylint: disable=redefined-argument-from-local
# pylint: disable=too-many-branches

class Sudoku:
    """The class object"""
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.size = len(grid)
        self.box_size = self.size // int(math.sqrt(self.size))
        # create a grid of viable candidates for each position
        candidates = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if grid[i][j] == 0:
                    row.append(self.find_options(i, j))
                else:
                    row.append(set())
            candidates.append(row)
        self.candidates = candidates

    def __repr__(self) -> str:
        representation = ''
        for row in self.grid:
            representation += str(row) + '\n'
        return representation

    def get_row(self, row: int) -> List[int]:
        """Getting the row"""
        return self.grid[row]

    def get_col(self, col: int) -> List[int]:
        """Getting the col"""
        return [row[col] for row in self.grid]

    def get_box_inds(self, row: int, col: int) -> List[Tuple[int, int]]:
        """Getting the boxes"""
        inds_box = []
        i_0 = (row // self.box_size) * self.box_size  # get first row index
        j_0 = (col // self.box_size) * self.box_size  # get first column index
        for i in range(i_0, i_0 + self.box_size):
            for j in range(j_0, j_0 + self.box_size):
                inds_box.append((i, j))
        return inds_box

    def get_box(self, row: int, col: int) -> List[int]:
        """Getting a lit of boxes"""
        box = []
        for i, j in self.get_box_inds(row, col):
            box.append(self.grid[i][j])
        return box

    def find_options(self, row: int, col: int) -> Set:
        """Finding candidates"""
        nums = set(range(1, self.size + 1))
        set_row = set(self.get_row(row))
        set_col = set(self.get_col(col))
        set_box = set(self.get_box(row, col))
        used = set_row | set_col | set_box
        valid = nums.difference(used)
        return valid

    def place_and_erase(self, row: int, col: int, number: int, constraint_prop=True):
        """ remove x as a candidate in the grid in this row, column and box"""
        # place candidate x
        self.grid[row][col] = number
        self.candidates[row][col] = set()
        # remove candidate x in neighbours
        inds_row = [(row, j) for j in range(self.size)]
        inds_col = [(i, col) for i in range(self.size)]
        inds_box = self.get_box_inds(row, col)
        erased = [(row, col)]  # set of indices for constraint propagation
        erased += self.erase([number], inds_row + inds_col + inds_box, [])
        # constraint propagation, through every index that was changed
        while erased and constraint_prop:
            i, j = erased.pop()
            inds_row = [(i, j) for j in range(self.size)]
            inds_col = [(i, j) for i in range(self.size)]
            inds_box = self.get_box_inds(i, j)
            for inds in [inds_row, inds_col, inds_box]:
                # apply strategies
                # 1. hidden singles
                uniques = self.get_unique(inds)
                for inds_unique, number in uniques:
                    i_u, j_u = inds_unique[0]
                    self.candidates[i_u][j_u] = set(number)
                    erased += self.erase(number, inds, inds_unique)

    def erase(self, nums, indices, keep):
        """ erase nums as candidates in indices, but not in keep"""
        erased = []
        for i, j in indices:
            edited = False
            if (i, j) in keep:
                continue
            for num in nums:
                if num in self.candidates[i][j]:
                    self.candidates[i][j].remove(num)
                    edited = True
            if edited:
                erased.append((i, j))
        return erased

    def count_candidates(self, indices):
        """Counting candidates"""
        count = [[] for _ in range(self.size + 1)]
        for i, j in indices:
            for num in self.candidates[i][j]:
                count[num].append((i, j))
        return count

    def get_unique(self, indices):
        """Getting unique candidates"""
        groups = self.count_candidates(indices)
        uniques = []  # final set of unique candidates to return
        for num, group_inds in enumerate(groups):
            if len(group_inds) == 1:
                uniques.append((group_inds, [num]))
        return uniques


def solve_sudoku(grid: List[List[int]], all_solutions: bool = False) \
        -> Tuple[List[List[int]], bool, Dict[str, int]]:
    """Solving the sudoku"""
    def solve(our_puzzle, depth=0) -> bool:
        """Solver method"""
        nonlocal calls, depth_max
        calls += 1
        depth_max = max(depth, depth_max)
        is_solved = False
        while not is_solved:
            is_solved = True
            edited = False  # if no edits, either done or stuck
            for i in range(size):
                for j in range(size):
                    if our_puzzle.grid[i][j] == 0:
                        is_solved = False
                        options = our_puzzle.candidates[i][j]
                        if len(options) == 0:
                            return False  # this call is going nowhere
                        if len(options) == 1:  # Step 1
                            our_puzzle.place_and_erase(i, j, list(options)[0])  # Step 2
                            edited = True
            if not edited:  # changed nothing in this round -> either done or stuck
                if is_solved:
                    solution_set.append(our_puzzle.grid)
                    return True
                # Find the square with the least number of options
                min_guesses = (size + 1, -1)
                for i in range(size):
                    for j in range(size):
                        options = our_puzzle.candidates[i][j]
                        if len(options) > 1:
                            min_guesses = min((len(options), (i, j)), min_guesses)
                i, j = min_guesses[1]
                options = our_puzzle.candidates[i][j]
                for option in options:  # step 3. backtracking check point:
                    puzzle_next = deepcopy(our_puzzle)
                    puzzle_next.place_and_erase(i, j, option)
                    is_solved = solve(puzzle_next, depth=depth + 1)
                    if is_solved and not all_solutions:
                        break  # return 1 solution
                return is_solved
        return is_solved

    calls, depth_max = 0, 0
    solution_set: List[List[int]] = []
    puzzle = Sudoku(grid)
    size = puzzle.size

    solved = solve(puzzle, depth=0)
    info = {'calls': calls,
            'max depth': depth_max,
            'nsolutions': len(solution_set),
            }

    return solution_set, solved, info


def flatten(grid) -> List[int]:
    """Flatten the grid"""
    arr = []
    for row in grid:
        arr.extend(row)
    return arr


def unflatten(arr: List[int]) -> List[List[int]]:
    """Unflatten the grid"""
    num: int = int(math.sqrt(len(arr)))
    grid = []
    for i in range(0, len(arr), num):
        grid.append(arr[i:i + num])
    return grid


def arr2str(arr: List[int]) -> str:
    """Convert arr to string"""
    string = ''
    for digit in arr:
        string += str(digit)
    return string


def str2arr(string: str) -> List[int]:
    """Convert string to arr"""
    arr = []
    end = string.find('-')
    end = len(string) if end == -1 else end
    for char in string[0:end]:
        if char == '0':
            arr.append(0)
        else:
            arr.append(int(char))
    return arr


def grid2str(grid: List[List[int]]) -> str:
    """Convert grid to string"""
    return arr2str(flatten(grid))


def str2grid(string: str) -> List[List[int]]:
    """Convert string to grid"""
    return unflatten(str2arr(string))
