import streamlit as st

def print_board(board):
    for row in board:
        st.write(" | ".join(row))
        st.write("-" * 5)

def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        row = st.number_input(f"Player {player}, enter row number (0, 1, or 2): ", min_value=0, max_value=2, step=1)
        col = st.number_input(f"Player {player}, enter column number (0, 1, or 2): ", min_value=0, max_value=2, step=1)

        if board[row][col] == ' ':
            board[row][col] = player
        else:
            st.write("That position is already taken. Try again.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            st.write(f"Player {winner} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            st.write("It's a draw!")
            break

        # Switch player
        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    st.title("Tic-Tac-Toe Game")
    play_game()
