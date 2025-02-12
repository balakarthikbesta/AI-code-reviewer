import streamlit as st
import google.generativeai as genai

# Configure Google AI API
genai.configure(api_key="AIzaSyDV4WzJV0KQlCAk1cwf1fqC5wW_i4WAyM4")

# Set up the AI model
sys_prompt = """
You are an AI code reviewer. You will analyze Python code for potential bugs, errors,
and areas of improvement. Provide detailed feedback and suggest fixes.
"""

model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp", 
                              system_instruction=sys_prompt)

def review_code(user_code):
    """Send user code to the AI model for review and return the response."""
    response = model.generate_content(user_code)
    return response.text

# Streamlit UI setup
st.title("AI Code Reviewer")
st.write("Submit your Python code for review and receive feedback!")

user_code = st.text_area("Enter your Python code here:")

if st.button("Review Code"):
    if user_code.strip():
        feedback = review_code(user_code)
        st.subheader("Review Feedback:")
        st.markdown(feedback)
    else:
        st.warning("Please enter some Python code before submitting.")
