import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()
#Hugging Face token
token = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
headers = {"Authorization": f"Bearer {token}"}
def query_model(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return f"Error {response.status_code}: {response.text}"

#Streamlit App UI
st.set_page_config(page_title="TalentScout Assistant")
st.title("TalentScout Hiring Assistant (AI/ML Intern Project)")
st.markdown("_This chatbot collects candidate info and generates tailored technical questions._")

#Candidate Form
with st.form("candidate_form"):
    st.subheader("Candidate Information")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.number_input("Years of Experience", min_value=0)
    position = st.text_input("Desired Position")
    location = st.text_input("Current Location")
    tech_stack = st.text_area("Tech Stack (e.g., Python, Django, SQL)")

    submitted = st.form_submit_button("Submit")

#click On Submit
if submitted:
    st.success(f"Thank you {name}! Generating questions...")

    prompt = f"""
    You are an AI Hiring Assistant. Generate 5 interview questions for a candidate with the following tech stack: {tech_stack}.
    Make the questions technical and tailored to the mentioned tools, languages, or frameworks.
    """

    with st.spinner("Thinking..."):
        response = query_model(prompt)
        st.subheader("Generated Technical Questions")
        st.write(response)

   
