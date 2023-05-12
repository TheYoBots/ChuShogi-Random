import random

# Board size
BOARD_SIZE = 12

# Function to initialize the game board
def initialize_board():
    board = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    return board

# Function to display the game board
def display_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Function to get a random legal move
def get_random_move(board):
    # Get all the positions of your pieces
    pieces = []
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 'X':
                pieces.append((i, j))
    
    # Select a random piece
    random_piece = random.choice(pieces)
    piece_row, piece_col = random_piece
    
    # Generate a random move for the selected piece
    possible_moves = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_row = piece_row + i
            new_col = piece_col + j
            if 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE and (i != 0 or j != 0):
                possible_moves.append((piece_row, piece_col, new_row, new_col))
    
    random_move = random.choice(possible_moves)
    return random_move

# Function to apply a move to the board
def make_move(board, move):
    src_row, src_col, dest_row, dest_col = move
    board[dest_row][dest_col] = board[src_row][src_col]
    board[src_row][src_col] = '.'

# Function to parse SFEN and set up the board
def parse_sfen(sfen):
    board = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    sfen_rows = sfen.split('/')
    row_index = 0
    for sfen_row in sfen_rows:
        col_index = 0
        for char in sfen_row:
            if char.isdigit():
                col_index += int(char)
            else:
                board[row_index][col_index] = char
                col_index += 1
        row_index += 1
    return board

# Function to parse a USI command
def parse_usi_command(command):
    global board  # Make the 'board' variable accessible within the function
    tokens = command.split()
    if tokens[0] == 'usi':
        print("id name ChuShogi Random")
        print("id author Yohaan Seth Nathan")
        print("usiok")
    elif tokens[0] == 'isready':
        print("readyok")
    elif tokens[0] == 'usinewgame':
        board = initialize_board()  # Initialize the board
    elif tokens[0] == 'position':
        if tokens[1] == 'startpos':
            board = initialize_board()  # Initialize the board
        else:
            # Parse the starting position
            sfen = ' '.join(tokens[1:])
            sfen_parts = sfen.split(' ')
            board = parse_sfen(sfen_parts[0])
            # Handle additional position setup commands if required
            pass
    elif tokens[0] == 'go':
        # Generate and make a move
        move = get_random_move(board)
        make_move(board, move)
        src_col, src_row, dest_col, dest_row = move
        usi_move = f"bestmove {chr(src_col + 97)}{src_row + 1}{chr(dest_col + 97)}{dest_row + 1}"
        print(usi_move)
    elif tokens[0] == 'quit':
        quit()

# Main game loop
def main():
    global board  # Make the 'board' variable accessible within the function
    board = initialize_board()  # Initialize the board
    try:
        while True:
            command = input()
            parse_usi_command(command)
    except KeyboardInterrupt:
        quit()

if __name__ == '__main__':
    main()
