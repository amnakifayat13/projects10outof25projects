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


# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1


st.markdown("<h1 style='color: rgb(90, 5, 62)'>🔍 Binary Search </h1>", unsafe_allow_html=True)
# Initialize the array
if "arr" not in st.session_state:
    st.session_state.arr = []

user_input = st.number_input("Enter an array element", value=0, step=1, format="%d")
if st.button("Submit"):
    st.session_state.arr.append(int(user_input))
    st.session_state.arr.sort()  
    st.write(st.session_state.arr)

# Get user input
st.session_state.x = st.number_input("Enter the number to search", value=0, step=1, format="%d")

# Function call
if st.button("Search"):
    result = binary_search(st.session_state.arr, 0, len(st.session_state.arr) - 1, st.session_state.x)

    if result != -1:
        st.success(f"Element is present at index {result}")
    else:
        st.error("Element is not present in array")