import streamlit as st
import numpy as np

# Custom Styling
st.markdown("""
    <style>
        
        .stButton>button {
            background-color: rgb(90, 5, 62);
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: rgb(63, 5, 37);
        }
    </style>
""", unsafe_allow_html=True)

def check_winner(board):
    for row in board:
        if all(cell == 'X' for cell in row):
            return 'X'
        if all(cell == 'O' for cell in row):
            return 'O'
    
    for col in board.T:
        if all(cell == 'X' for cell in col):
            return 'X'
        if all(cell == 'O' for cell in col):
            return 'O'
    
    if all(board[i, i] == 'X' for i in range(3)) or all(board[i, 2 - i] == 'X' for i in range(3)):
        return 'X'
    if all(board[i, i] == 'O' for i in range(3)) or all(board[i, 2 - i] == 'O' for i in range(3)):
        return 'O'
    
    if not any(cell == '' for row in board for cell in row):
        return 'Draw'
    
    return None

def reset_game():
    st.session_state.board = np.full((3, 3), '', dtype=str)
    st.session_state.current_player = 'X'
    st.session_state.winner = None

def main():
    st.markdown("<h1 style='text-align: center; color:rgb(90, 5, 62);'>🟢❌⭕ Tic Tac Toe Game</h1>", unsafe_allow_html=True)

    # session state initialization
    if "board" not in st.session_state:
        reset_game()

    board = st.session_state.board
    current_player = st.session_state.current_player
    winner = st.session_state.winner

    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            if board[i, j] == '':
                if cols[j].button(" ", key=f"{i}-{j}") and not winner:
                    board[i, j] = current_player
                    st.session_state.current_player = 'O' if current_player == 'X' else 'X'
                    st.session_state.winner = check_winner(board)
                    st.rerun()
            else:
                cols[j].write(f"**{board[i, j]}**")
                

    if winner:
        if winner == 'Draw':
            st.success("It's a Draw!")
        else:
            st.success(f"Player {winner} wins!")
        if st.button("Restart Game"):
            reset_game()
            st.rerun()

if __name__ == "__main__":
    main()
