import streamlit as st
from PIL import Image

# Set the title of the application
st.title("Image Display Application")

# Upload the image you want to display
image_path = "your_image.jpg"  # Replace with the name of your image file

try:
    # Load and display the image
    image = Image.open(image_path)
    st.image(image, caption="Displayed Image", use_column_width=True)
except FileNotFoundError:
    st.error("Image file not found. Please make sure the image is in the same directory as this script.")

# Add a file uploader to optionally upload and view another image
uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_image:
    uploaded = Image.open(uploaded_image)
    st.image(uploaded, caption="Uploaded Image", use_column_width=True)

