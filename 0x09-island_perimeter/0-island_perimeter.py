#!/usr/bin/python3
"""Island Perimeter Problem
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a rectangular grid.

    The grid is a list of lists of integers where 0 represents water and 1 repre    sents land.
    The island is connected horizontally/vertically (not diagonally) and has no     lakes.
    The grid is completely surrounded by water and there is only one island.
    The function returns an integer representing the perimeter of the island.

    Parameters:
    - grid: A rectangular grid of 0s and 1s representing water and land.

    Returns:
    - An integer representing the perimeter of the single island present in the     grid.
    """

    perimeter = 0
    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if i == n-1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if j == m-1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
