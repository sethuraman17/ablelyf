import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="AbleLyf - Empowering Lives",
    page_icon="✨",
    layout="centered",
)

# Header
st.title("Welcome to AbleLyf")

# Navigation
nav_selection = st.sidebar.radio("Navigate", ["Home", "Products", "Contact Us"])

# Home Page
if nav_selection == "Home":
    st.write(
        "Empowering lives through accessible technology. At AbleLyf, we believe in creating innovative solutions for individuals facing diverse challenges."
    )

# Products Page
elif nav_selection == "Products":
    st.subheader("Our Products")

    st.write("1. **AbleToExpress**:")
    st.write(
        "If you're visually impaired, AbleToExpress is here to assist. Our Android app provides a voice-assisted path guide and object recognition to help you navigate your surroundings effortlessly."
    )

    st.write("2. **AbleToSee**:")
    st.write(
        "Designed for individuals with disabilities affecting hand movement, AbleToSee uses iris tracking for cursor control. Blink to click, giving you control over your device using eye movements."
    )

    st.write("3. **MoodSynthesizer**:")
    st.write(
        "MoodSynthesizer understands and interprets emotions. It's an innovative tool that analyzes a person's mood, enhancing communication and interaction with those around them."
    )

# Contact Us Page
elif nav_selection == "Contact Us":
    st.subheader("Contact Us")

    st.write(
        "Have questions or want to learn more about our products and services? Reach out to us!"
    )

    st.info("Email: info@ablelyf.com\nPhone: +1 (555) 123-4567")

# Footer
st.sidebar.markdown(
    """
    ---
    © 2023 AbleLyf. All rights reserved.
    """
)
