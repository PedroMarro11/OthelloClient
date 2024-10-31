from othello_client.intelligence import *
import timeit

def initialize_board():
    board = [[0] * 8 for _ in range(8)]
    
    board[3][3], board[4][4] = 1, 1
    board[3][4], board[4][3] = -1, -1
    return board

def print_board(board):
    print("  " + " ".join(map(str, range(8))))
    for i, row in enumerate(board):
        print(f"{i} " + " ".join('X' if x == 1 else 'O' if x == -1 else '.' for x in row))

def game_loop():
    timer = timeit.default_timer
    board = initialize_board()
    current_player = -1  
    while True:
        moves = valid_moves(board, current_player)
        if not moves:
            print("No hay movimientos validos.")
            break

        if current_player == 1:
            print("Turno de X:")
            print_board(board)
            row, col = map(int, input("Movimiento (row col): ").split())
            while (row, col) not in moves:
                print("Movimiento inválido.")
                row, col = map(int, input("Movimiento (row col): ").split())
        else:
            print("turno de AI's (O):")
            print_board(board)
            move_start = timer()
            row, col = AI_MOVE(board, current_player)
            move_end = timer()
            print(f"Movimiento de AI: {row} {col}, en {move_end - move_start:.2f} segundos.")

        make_move(board, current_player, row, col)
        current_player = -current_player  

    print_board(board)

game_loop()