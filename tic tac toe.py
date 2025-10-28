def print_board(board):
    display = [str(i+1) if cell == ' ' else cell for i, cell in enumerate(board)]
    print(f"\n {display[0]} | {display[1]} | {display[2]} ")
    print("---+---+---")
    print(f" {display[3]} | {display[4]} | {display[5]} ")
    print("---+---+---")
    print(f" {display[6]} | {display[7]} | {display[8]} \n")

def check_win(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def get_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player} ({'X' if player == 'X' else 'O'}), choose your position (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9.")
            elif board[move] != ' ':
                print("That position is already taken. Choose another.")
            else:
                return move
        except ValueError:
            print("Invalid input. Try again with a number between 1 and 9.")

def tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'
    moves = 0

    print("Welcome to Tic Tac Toe!\n")
    print_board(board)

    while True:
        move = get_move(board, current_player)
        board[move] = current_player
        print_board(board)
        moves += 1

        if check_win(board, current_player):
            print(f"Congratulations, Player {current_player} wins!")
            break
        if moves == 9:
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
