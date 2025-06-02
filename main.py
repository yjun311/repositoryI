import streamlit as st

st.title("틱택토 게임 🎮")

# 세션 상태 초기화
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
if "turn" not in st.session_state:
    st.session_state.turn = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

def check_winner(board):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in win_conditions:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "무승부"
    return None

def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.ses

