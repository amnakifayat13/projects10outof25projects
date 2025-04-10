import random
import streamlit as st
from words import words
from hangman_visual import lives_visual_dict

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


# Session State
def initialization():
    if "secret_word" not in st.session_state:
        st.session_state.secret_word = random.choice(words)

    if "store_dash" not in st.session_state:
        st.session_state.store_dash = ["_"] * len(st.session_state.secret_word)

    if "lives" not in st.session_state:
        st.session_state.lives = 7

# display the game
def display_game():
    change_in_string = " ".join(st.session_state.store_dash)
    st.write("Guess Word:", change_in_string) 
    container = st.container(border=True)
    container.code(f"```\n{lives_visual_dict[st.session_state.lives]}```\n")
    container.write(f"Lives: {st.session_state.lives}")


# guess process
def guess_process(user_guess):
    if st.button("Submit Letter"):
        find_letter = st.session_state.secret_word.find(user_guess)
        
        if st.session_state.lives == 0:
            st.title("Game Over 😢")
            st.subheader(f"The correct word was: {st.session_state.secret_word}")
            return  
        
        if find_letter == -1:
            st.write("Letter is not available")
            st.session_state.lives -= 1
            
        else:
            for index, letter in enumerate(st.session_state.secret_word):
                if letter == user_guess:
                    st.session_state.store_dash[index] = user_guess
            st.write("Current Word State:", "".join(st.session_state.store_dash))  # Debugging


            if "_" not in st.session_state.store_dash:
                st.success("Congratulations! You guessed the word 🎉")
                st.rerun()

        st.rerun()


def reset_game():
    if st.button("Reset Game"):
        st.session_state.secret_word = random.choice(words)
        st.session_state.store_dash = ["_"] * len(st.session_state.secret_word)
        st.session_state.lives = 7
        st.rerun()


def main():
    initialization()
    st.markdown("<h1 style='color: rgb(90, 5, 62)'>🔠 Hangman Game </h1>", unsafe_allow_html=True)
    display_game()
    user_guess = st.text_input("Guess a letter")
    col1,col2 = st.columns(2)
    with col1:
        guess_process(user_guess)
    with col2:
        reset_game()  

main()
