#!/usr/bin/python3
"""The N-queens puzzle"""

import sys


def board_init(n):
    """Initialize an `n`x`n` sized chessboard with 0's.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list: A list of lists representing the initialized chessboard.
    """
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return board


def board_deepcopy(board):
    """Return a deepcopy of a chessboard.

    Args:
        board (list): The chessboard to copy.

    Returns:
        list: A deepcopy of the chessboard.
    """
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board


def get_solution(board):
    """Return the list of lists representation in a board.

    Args:
        board (list): The chessboard.

    Returns:
        list: A list of positions of queens on the board.
    """
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def xout(board, row, col):
    """Mark out spots on a chessboard.

    Args:
        board (list): The chessboard.
        row (int): The row position of the queen.
        col (int): The column position of the queen.
    """
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The chessboard.
        row (int): The current row being checked.
        queens (int): The number of queens placed on the board.
        solutions (list): The list of solutions.

    Returns:
        list: The list of solutions.
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = board_init(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)

