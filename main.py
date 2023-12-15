import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="MAVINS - Empowering Lives",
    page_icon="✨",
    layout="centered",
)

# Header
st.title("Welcome to MAVINS")

# Navigation
nav_selection = st.sidebar.radio("Navigate", ["Home", "Products", "Contact Us"])

# Home Page
if nav_selection == "Home":
    st.write(
        "Empowering lives through accessible technology. At MAVINS, we believe in creating innovative solutions for individuals facing diverse challenges."
    )

# Products Page
elif nav_selection == "Products":
    st.subheader("Our Products")

    st.write("1. **Autism Behaviour Analysis**:")
    st.write(
        "There will be a AI who work as a analyzer for autism students by analysing their behaviour such as hand flapping, bitting, etc... and make and excel data of that."
    )

    st.write("2. **Face Attendance**:")
    st.write(
        "This will be a Face Attendance and registration system that we can use in Autism Schools and once a face of the student detected and recognized then thevideo will play for each student to make happy them."
    )

# Contact Us Page
elif nav_selection == "Contact Us":
    st.subheader("Contact Us")

    st.write(
        "Have questions or want to learn more about our products and services? Reach out to us!"
    )

    st.info("Email: sethuramanvr046@gmail.com\nPhone: +91 9344785652")

# Footer
st.sidebar.markdown(
    """
    ---
    © 2023 MAVINS. All rights reserved.
    """
)
