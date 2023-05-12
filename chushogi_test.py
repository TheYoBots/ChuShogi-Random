import random

class ChuShogiEngine:

    def __init__(self):
        self.board = [[None for i in range(12)] for j in range(12)]
        self.turn = 0

    def make_move(self):
        # Get a random move from the list of possible moves.
        possible_moves = self.get_possible_moves()
        move = random.choice(possible_moves)

        # Make the move.
        self.board[move[0]][move[1]] = self.turn
        self.turn = 1 - self.turn

        return move

    def get_possible_moves(self):
        # Get a list of all possible moves.
        possible_moves = []
        for i in range(12):
            for j in range(12):
                if self.board[i][j] is not None and self.board[i][j] == self.turn:
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            if di == 0 and dj == 0:
                                continue
                            ni = i + di
                            nj = j + dj
                            if 0 <= ni < 12 and 0 <= nj < 12 and self.board[ni][nj] is None:
                                possible_moves.append((i, j, ni, nj))
        return possible_moves

    def is_game_over(self):
        # Check if the game is over.
        for i in range(12):
            for j in range(12):
                if self.board[i][j] is not None and self.board[i][j] == self.turn:
                    return False
        return True

    def get_winner(self):
        # Get the winner of the game.
        if self.is_game_over():
            if self.turn == 0:
                return "Black"
            else:
                return "White"
        else:
            return None

    def usi_protocol(self):
        while True:
            # Get a command from the user.
            command = input()

            # Parse the command.
            command_parts = command.split()

            # Check the command.
            if command_parts[0] == "usi":
                print("id name ChuShogi Random")
                print("id author Yohaan Seth Nathan")
                print("usiok")
            elif command_parts[0] == "isready":
                print("readyok")
            elif command_parts[0] == "new":
                self.board = [[None for i in range(12)] for j in range(12)]
                self.turn = 0
                print("ok")
            elif command_parts[0] == "position":
                board_string = command_parts[1]
                for i in range(12):
                    for j in range(12):
                        self.board[i][j] = board_string[i * 12 + j]
                self.turn = board_string[12 * 12]
                print("ok")
            elif command_parts[0] == "go":
                move = self.make_move()
                print("move " + str(move[0] + 1) + " " + str(move[1] + 1) + " " + str(move[2] + 1) + " " + str(move[3] + 1))
            elif command_parts[0] == "quit":
                break