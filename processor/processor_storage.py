#!/usr/bin/env python3
"""Database storage object"""

from typing import List


class Storage:
    def __init__(self):
        """Creating storage for JSON lists that will be returned"""
        # Variables.
        # List to store received grid.
        self._grids = []
        # List to store the returned results.
        self._grid_strings: List[str] = []

    @property
    def grids(self) -> List[List[int]]:
        """Return grid list"""
        return self._grids

    @property
    def grid_strings(self) -> List[str]:
        """Return string of results"""
        return self._grid_strings
