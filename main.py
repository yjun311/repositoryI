import streamlit as st

st.title("틱택토 게임")

# 초기 게임판 상태 저장
if "board" not in st.session_state:
    st.session_state.board = [""] * 9  # 3x3판을 1차원 리스트로 표현
if "turn" not in st.session_state:
    st.session_state.turn = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

def check_winner(board):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),  # 가로
        (0,3,6), (1,4,7), (2,5,8),  # 세로
        (0,4,8), (2,4,6)            # 대각선
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "무승부"
    return None

def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None

if st.session_state.winner:
    if st.session_state.winner == "무승부":
        st.info("무승부입니다!")
    else:
        st.success(f"{st.session_state.winner} 승리!")
    if st.button("다시 시작"):
        reset_game()
else:
    cols = st.columns(3)
    for i in range(9):
        col = cols[i % 3]
        if col.button(st.session_state.board[i] or " ", key=i):
            if st.session_state.board[i] == "" and st.session_state.winner is None:
                st.session_state.board[i] = st.session_state.turn
                winner = check_winner(st.session_state.board)
                if winner:
                    st.session_state.winner = winner
                else:
                    st.session_state.turn = "O" if st.session_state.turn == "X" else "X"

    st.write(f"현재 차례: {st.session_state.turn}")
