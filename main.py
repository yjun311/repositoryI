import streamlit as st

st.markdown("""
    <style>
    .tic-tac-toe-button {
        font-size: 2rem;
        width: 80px;
        height: 80px;
        margin: 5px;
        border-radius: 10px;
        border: 2px solid #333;
        background-color: #fafafa;
    }
    .tic-tac-toe-button:hover {
        background-color: #e0f7fa;
        cursor: pointer;
    }
    .turn-info {
        font-size: 1.5rem;
        margin-top: 20px;
        font-weight: bold;
        color: #00796b;
    }
    .winner-info {
        font-size: 2rem;
        margin: 20px 0;
        color: #d32f2f;
        font-weight: bold;
    }
    .restart-button {
        margin-top: 20px;
    }
    .board {
        display: flex;
        flex-wrap: wrap;
        width
