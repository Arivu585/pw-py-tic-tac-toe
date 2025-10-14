# Tic Tac Toe Game in Python

# Create the board (list of 9 spaces)
board = [' ' for _ in range(9)]

# Print the current board
def print_board():
    print()
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            print("---|---|---")
    print()

# Check for a win
def check_win(symbol):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == symbol for i in condition):
            return True
    return False

# Check for draw
def check_draw():
    return ' ' not in board

# Take player input
def player_move(symbol):
    while True:
        try:
            position = int(input(f"Player {symbol}, enter position (1-9): ")) - 1
            if position < 0 or position > 8:
                print("Invalid position. Choose 1–9.")
            elif board[position] != ' ':
                print("That spot is taken. Try again.")
            else:
                board[position] = symbol
                break
        except ValueError:
            print("Please enter a number between 1 and 9.")

# Main game loop
def play_game():
    current_symbol = 'X'
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        player_move(current_symbol)
        print_board()

        if check_win(current_symbol):
            print(f"🎉 Player {current_symbol} wins!")
            break
        elif check_draw():
            print("It's a draw!")
            break
        else:
            current_symbol = 'O' if current_symbol == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    play_game()
