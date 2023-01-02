#!/usr/bin/python3
"""The N queens Task by ALX"""
import sys



def init_board(n):
    """Initializes an nxn board"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)

def board_deepcopy(board):
    """Returns a deepcopy of the board"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)

def get_solution(board):
    """This func returns the solutions of the chessboard in list type"""
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "Q":
                solution.append([i, j])
                break
    return solution

def xout(board, row, col):
    """X'ed out spots on a chessboard"""

    #X out forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "X"

    #X out backward spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"

    #X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"

    #X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"

    #X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1

    #X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1

    #X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1

    #X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solves the N-queens puzzle."""
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


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

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
