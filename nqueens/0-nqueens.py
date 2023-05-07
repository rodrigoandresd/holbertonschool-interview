#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an NxN chessboard.
Write a program that solves the N queens problem.
"""
from sys import argv


def print_board(board):
    for row in board:
        print(row)

def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve(board, col):
    # base case: all queens are placed
    if col >= N:
        print_board(board)
        print()
        return True
    # try to place a queen in each row of the current column
    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve(board, col + 1)
            board[row][col] = 0
    # if no solution is found
    return False

if __name__ == "__main__":
    # parse command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    # initialize the chessboard
    board = [[0 for x in range(N)] for y in range(N)]
    # solve the N queens problem
    solve(board, 0)
