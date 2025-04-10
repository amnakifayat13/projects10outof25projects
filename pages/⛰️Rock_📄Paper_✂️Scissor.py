import streamlit as st
import random

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

st.markdown("<h1 style='color: rgb(90, 5, 62);'>📄Paper, ⛰️Rock & ✂️Scissor Game</h1>", unsafe_allow_html=True)

# Add a placeholder option
user_action = st.selectbox("Enter a choice:", ["Select an option", "Rock", "Paper", "Scissor"])

# Ensure the game logic only runs if a valid choice is made
if user_action != "Select an option":
    possible_actions = ["Rock", "Paper", "Scissor"]
    computer_action = random.choice(possible_actions)
    st.write(f"You chose {user_action}, computer chose {computer_action}.")

    if user_action == computer_action:
        st.write(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "Rock":
        if computer_action == "Scissor":
            st.balloons()
            st.success("Rock smashes Scissor! You win!")
        else:
            st.write("Paper covers Rock! You lose.")
    elif user_action == "Paper":
        if computer_action == "Rock":
            st.balloons()
            st.success("Paper covers Rock! You win!")
        else:
            st.write("Scissor cuts Paper! You lose.")
    elif user_action == "Scissor":
        if computer_action == "Paper":
            st.balloons()
            st.success("Scissor cuts Paper! You win!")
        else:
            st.write("Rock smashes Scissor! You lose.")