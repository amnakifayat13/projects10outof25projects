import streamlit as st
import re
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    score = 0
    messages = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        messages.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        messages.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        messages.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    st.markdown("---")
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    colors = ["red", "orange", "yellow", "green", "darkgreen"]
    
    # Rainbow progress bar
    rainbow_colors = ["#ff0000", "#ff7f00", "#ffff00", "#00ff00", "#0000ff"]
    st.markdown(f"""<div style='width: 100%; height: 20px; background: linear-gradient(to right, {', '.join(rainbow_colors[:score+1])}); border-radius: 10px;'></div>""", unsafe_allow_html=True)
    
    st.markdown(f"<p style='color:{colors[score]}; font-size:20px;'>🔒 {strength_levels[score]} Password (Score: {score}/4)</p>", unsafe_allow_html=True)
    
    # Password Analysis
    st.markdown("### Password Analysis")
    if score == 4:
        st.markdown("✅ Your password is strong and secure!")
    else:
        for msg in messages:
            st.markdown(f"<p style='color:red;'>{msg}</p>", unsafe_allow_html=True)

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

# Title & Input Field
st.markdown("<h1 style='text-align: center; color:rgb(90, 5, 62);'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)
password = st.text_input("Enter your password:", type="password")

# Button to check password strength
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        suggested_password = generate_password()
        st.markdown(f"<p style='color:blue; font-size:16px;'>💡 Enter a Password? Suggest this one: <b>{suggested_password}</b></p>", unsafe_allow_html=True)

# -------------------------------
# Feedback Section
# -------------------------------
st.markdown("---")
st.markdown("### 📝 Feedback")
feedback = st.text_area("Tell us how we can improve this tool:")

if st.button("Submit Feedback"):
    if feedback:
       
        st.success("✅ Thank you for your feedback!")
    else:
        st.warning("⚠️ Please enter some feedback before submitting.")
