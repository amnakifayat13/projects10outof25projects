import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO
import cv2
import numpy as np

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

st.markdown("<h1 style='text-align: center; color:rgb(90, 5, 62);'>🔳QR Code Encoder</h1>", unsafe_allow_html=True)

if 'data' not in st.session_state:
    st.session_state.data = ''

st.session_state.data = st.text_input('Enter the data to encode', st.session_state.data)

if st.button('Generate QR Code'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=7,
        border=1
    )
    qr.add_data(st.session_state.data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    # Save the QR code image to a BytesIO object
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    st.image(buffer, caption='QR Code', width=200)

    # Download button
    st.download_button(
        label="Download QR Code",
        data=buffer,
        file_name="qr_code.png",
        mime="image/png"
    )

if st.button("Reset"):
    st.session_state.data = ''
    st.rerun()

# QR code decoder
st.markdown("<h1 style='text-align: center; color:rgb(90, 5, 62);'>🔍QR Code Decoder</h1>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload a QR Code image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded QR Code', width=200)
    
    # Convert the uploaded image to a format compatible with OpenCV
    image_np = np.array(image.convert('RGB'))
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)

    # Decode the QR code using OpenCV
    detector = cv2.QRCodeDetector()
    decoded_data, points, _ = detector.detectAndDecode(gray_image)

    if decoded_data:
        st.write("Decoded Data: ", decoded_data)
    else:
        st.write("No QR code found in the image.")