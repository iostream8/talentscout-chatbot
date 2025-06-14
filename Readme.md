# TalentScout Hiring Assistant

A Streamlit-based chatbot that collects candidate information and generates relevant technical interview questions using Hugging Face LLM (`zephyr-7b-beta`).

##  Features
- Collects basic candidate details
- Generates 3–5 tailored technical questions based on candidate's tech stack
- Clean UI using Streamlit
- Uses Hugging Face hosted API for LLM inference

## Tech Stack
- Python
- Streamlit
- Hugging Face Transformers API

## Installation
```bash
git clone https://github.com/your-username/talentscout-chatbot.git
cd talentscout-chatbot
pip install -r requirements.txt
streamlit run app.py
