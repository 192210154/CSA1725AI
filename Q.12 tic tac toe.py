class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize the board
        self.current_winner = None  # Keep track of the winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
    
        row_index = square // 3
        row = self.board[row_index*3:(row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True5
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Top-left to bottom-right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Top-right to bottom-left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def play_game():
    game = TicTacToe()
    x_player = 'X'
    o_player = 'O'
    current_player = x_player

    while game.empty_squares():
        game.print_board_nums()
        print("\n")
        game.print_board()
        print("\n")
        available_moves = game.available_moves()
        move = None

        while move not in available_moves:
            move = int(input(f"{current_player}'s turn. Enter your move (0-8): "))
            if move not in available_moves:
                print("Invalid move. Try again.")

        game.make_move(move, current_player)

        if game.current_winner:
            print(f"{current_player} wins!")
            break

        current_player = o_player if current_player == x_player else x_player

    if not game.current_winner:
        print("It's a tie!")


if __name__ == "__main__":
    play_game()

