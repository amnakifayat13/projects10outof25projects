import streamlit as st

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


st.markdown("<h1 style='color: rgb(90, 5, 62)'>🏋️ BMI Calculator</h1>", unsafe_allow_html=True)

user_weight = st.number_input("Enter your weight in kg:", min_value=1.0, format="%.2f")

height_unit = st.selectbox("Choose your height unit:", ["meter", "centimeter", "millimeter", "feet"])
user_height = st.number_input("Enter your height value:", min_value=1.0, format="%.2f")

# BMI Calculation
if st.button("Calculate BMI"):
    if height_unit == "meter":
        bmi = user_weight / (user_height ** 2)
    elif height_unit == "centimeter":
        bmi = user_weight / ((user_height / 100) ** 2)
    elif height_unit == "millimeter":
        bmi = user_weight / ((user_height / 1000) ** 2)
    elif height_unit == "feet":
        bmi = user_weight / ((user_height * 0.3048) ** 2)
    else:
        st.write("Please select a valid height unit")
    st.success(f"Your BMI is: {round(bmi, 2)}")

# health check

    if bmi  < 18.5:
        st.warning("You are Underweight take care about your health!")
    elif bmi >= 18.5 and bmi <= 24.9:
        st.balloons()
        st.success("You are healthy")
    elif bmi >= 25 and bmi <= 29.9:
        st.warning("you are Overweight!")
    elif bmi >= 30 and bmi <= 34.9:
        st.warning("You are in Obesity (Class1)")
    elif bmi >= 35 and bmi <= 39.9:
        st.warning("You are in Obesity (Class2) you should concern about it...")
    elif bmi >= 40:
        st.error("Severe Obesity (Class 3) you must pay attention on your health!!!")



   
