import streamlit as st
from colorthief import ColorThief
from PIL import Image
import io

# Page setup
st.set_page_config(page_title="Color Classifier", layout="centered")
st.title("🎨 Image Color Classifier")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Open and resize image for display
    image = Image.open(uploaded_file)
    image.thumbnail((200, 200))  # Resize to fit 200px max
    st.image(image, caption="Uploaded Image", width=200)

    # Analyze color with loading spinner
    with st.spinner("Analyzing dominant color..."):
        uploaded_file.seek(0)  # Reset stream before reading
        color_thief = ColorThief(uploaded_file)
        dominant_color = color_thief.get_color(quality=1)

    # Show results
    st.success(f"Dominant Color: RGB {dominant_color}")
    st.markdown(
        f"<div style='width:100px;height:100px;background-color:rgb{dominant_color};"
        f"border:2px solid #000; margin-top: 10px;'></div>",
        unsafe_allow_html=True
    )
