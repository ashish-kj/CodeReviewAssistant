import streamlit as st
import requests

st.title("Code Review Assistant (DeepSeek)")

code_input = st.text_area("Paste your code here:", height=300)

if st.button("Get Review"):
    if code_input:
        with st.spinner("Getting review..."):
            try:
                response = requests.post("http://localhost:8000/review/", data={"code": code_input})
                response.raise_for_status()  # Raise an exception for bad status codes
                review = response.json().get("review", "No feedback returned.")
                st.subheader("Review & Suggestions:")
                st.code(review)
            except requests.exceptions.RequestException as e:
                st.error(f"Error contacting backend: {e}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please paste some code to review.")