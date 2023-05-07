#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an NxN chessboard.
Write a program that solves the N queens problem.
"""

import sys

def solveNQueens(n):
    # Initialize the board
    board = [[0 for j in range(n)] for i in range(n)]
    # Start with the first column
    return solveNQueensUtil(board, 0)

def solveNQueensUtil(board, col):
    # If all queens are placed, we have found a solution
    if col == len(board):
        return [board]
    solutions = []
    # Try placing a queen in each row of the current column
    for row in range(len(board)):
        if isSafe(board, row, col):
            board[row][col] = 1
            # Recursively solve the problem for the next column
            solutions += solveNQueensUtil(board, col + 1)
            # Backtrack
            board[row][col] = 0
    return solutions

def isSafe(board, row, col):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check if there is a queen in the upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check if there is a queen in the lower diagonal
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # If all checks pass, the position is safe
    return True

if __name__ == '__main__':
    solutions = solveNQueens(N)
    for solution in solutions:
        print(solution)
