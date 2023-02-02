#!/usr/bin/python3
"""
N queens puzzle
"""
import sys


def solve_n_queens(n):
    """ Backtracking algorithm to solve the N-Queens problem """
    def can_place(row, col):
        """
        checks if a queen can be placed in a particular row
        """
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(row = 0, placed = []):
        """
        recursive function that places queens in each row
        """
        if row == n:
            result.append(placed[:])
        for col in range(n):
            if can_place(row, col):
                board[row] = col
                backtrack(row + 1, placed + [col])

    board = [-1] * n
    result = []
    backtrack()
    return result

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

result = solve_n_queens(n)
for solution in result:
    print(" ".join(str(x) for x in solution))
