import streamlit as st
import time


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

st.markdown("<h1 style='color: rgb(90, 5, 62);'>🎉 ⏳Birthday Countdown Timer 🎂</h1>", unsafe_allow_html=True)
user_input = st.number_input("Enter the time in seconds:  " , min_value = 0 , step = 1)
def countdown(t):
    timer = st.empty()
    while t:
        mins, secs = divmod(t, 60)
        timer.write(f"⏳ Time left: {mins:02d}:{secs:02d}")
        time.sleep(1)
        t -= 1
        
    st.balloons()
    # st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/BirthdaySong.mp3")    
    st.write(" ### 🎉:rainbow[Happy Birthday To You!!!!!]🎂🥳")



if st.button("Start Countdown"):
    countdown(int(user_input))
    

  
