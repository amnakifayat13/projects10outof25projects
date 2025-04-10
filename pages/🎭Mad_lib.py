import streamlit as st
from datetime import datetime

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

import streamlit as st

import streamlit as st

def main():
    st.markdown("<h1 style='color: rgb(90, 5, 62)'>✨ Mad Libs Adventure 🎭 </h1>", unsafe_allow_html=True)
    st.subheader("Fill in the blanks by choosing words to create an exciting story! 📖")
    
    # User choices
    noun = st.selectbox("🔤 Choose a noun:", ["dog 🐶", "robot 🤖", "pirate ☠️", "wizard 🧙"])
    adjective = st.selectbox("🎨 Choose an adjective:", ["happy 😊", "furious 😡", "magical ✨", "brave 🦸"])
    verb = st.selectbox("⚡ Choose a verb:", ["run 🏃", "dance 💃", "fly 🕊️", "explore 🔍"])
    place = st.selectbox("🌍 Choose a place:", ["forest 🌳", "castle 🏰", "ocean 🌊", "space 🚀"])
    
    # Generate story when selections are made
    if noun and adjective and verb and place:
        story = (
            f"📜 Once upon a time, in a faraway land, a {adjective} {noun} lived. "
            f"One day, it decided to {verb} all the way to the {place}. 🌎\n\n"
            f"Upon reaching the {place}, the {noun} discovered a hidden treasure chest 🎁. "
            f"But suddenly, a giant appeared! 🏔️ The {adjective} {noun} had to think fast.\n\n"
            f"Using its wits and courage, the {noun} found a secret passage and escaped. "
            f"In the end, it learned that true adventure lies in the journey, not the destination. ✨"
        )
        
        st.subheader("🎉 Your Mad Lib Adventure:")
        st.write(story)
    
if __name__ == "__main__":
    main()

