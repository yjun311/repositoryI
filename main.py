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
    st.session_state.winner = None

# 버튼 스타일 (크기와 글자 크기)
st.markdown("""
<style>
div.stButton > button {
    height: 70px;
    width: 70px;
    font-size: 2rem;
    margin: 4px;
}
</style>
""", unsafe_allow_html=True)

if st.session_state.winner:
    if st.session_state.winner == "무승부":
        st.success("무승부입니다! 🤝")
    else:
        st.success(f"{st.session_state.winner} 승리! 🎉")
    if st.button("다시 시작"):
        reset_game()
else:
    for row in range(3):
        cols = st.columns(3)
        for col in range(3):
            idx = row * 3 + col
            label = st.session_state.board[idx] if st.session_state.board[idx] != "" else " "
            if cols[col].button(label, key=idx):
                if st.session_state.board[idx] == "" and st.session_state.winner is None:
                    st.session_state.board[idx] = st.session_state.turn
                    winner = check_winner(st.session_state.board)
                    if winner:
                        st.session_state.winner = winner
                    else:
                        st.session_state.turn = "O" if st.session_state.turn == "X" else "X"

    st.markdown(f"### 현재 차례: **{st.session_state.turn}**")
