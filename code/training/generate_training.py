from board import Board


def dfs(board):
    n = len(board)
    board[0][0] = 1
    curr = board[0][0]
    while has_neighbors(curr):
        pass
    return board