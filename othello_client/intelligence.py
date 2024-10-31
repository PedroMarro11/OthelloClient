import random


def is_valid_move(board, player, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    if board[row][col] != 0:
        return False

    opponent = -player

    for direction in directions:
        dr, dc = direction
        r, c = row + dr, col + dc
        found_opponent = False

        while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
            r += dr
            c += dc
            found_opponent = True

        if found_opponent and 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
            return True

    return False
def valid_moves(board, player):
    valid_moves = []
    for row in range(8):
        for col in range(8):
            if is_valid_move(board, player, row, col):
                valid_moves.append((row, col))

    return valid_moves

def AI_MOVE(board, player):
    _valid_moves = valid_moves(board, player)
    best_immediate_move = None
    for move in _valid_moves:
        if best_immediate_move is None:
            best_immediate_move = move
        elif flipped_pieces(board, player, *move) > flipped_pieces(board, player, *best_immediate_move):
            best_immediate_move = move
    row = best_immediate_move[0]
    col = best_immediate_move[1]
    return (row, col)

def flipped_pieces(board, player, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    opponent = -player
    flipped = []

    for direction in directions:
        dr, dc = direction
        r, c = row + dr, col + dc
        found_opponent = False
        pieces_to_flip = []

        while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
            pieces_to_flip.append((r, c))
            r += dr
            c += dc
            found_opponent = True

        if found_opponent and 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
            flipped.extend(pieces_to_flip)

    return len(flipped)

def make_move(board, player, row, col):
    board[row][col] = player
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    opponent = -player

    for direction in directions:
        dr, dc = direction
        r, c = row + dr, col + dc
        found_opponent = False

        while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
            r += dr
            c += dc
            found_opponent = True

        if found_opponent and 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
            r, c = row + dr, col + dc
            while board[r][c] == opponent:
                board[r][c] = player
                r += dr
                c += dc

    return board