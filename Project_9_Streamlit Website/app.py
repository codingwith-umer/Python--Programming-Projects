import streamlit as st

# Title of the Website
st.title("Welcome to My First Streamlit Website!")

# Subtitle
st.subheader("A Simple Python Project")

# Input from the User
name = st.text_input("Enter your name:", placeholder="")

# Button to Submit
if st.button("Greet Me!"):
    if name:
        st.success(f"Hello, {name}! 👋 Welcome to this simple Streamlit app!")
    else:
        st.error("Please enter your name to get a greeting.")

# Additional Content
st.write("This is a basic Streamlit app designed to demonstrate how to build a simple website using Python.")
st.markdown("### Features:")
st.markdown("- Interactive user input")
st.markdown("- Dynamic output display")

st.write("Streamlit makes creating websites in Python fun and easy!🤩 🚀")
