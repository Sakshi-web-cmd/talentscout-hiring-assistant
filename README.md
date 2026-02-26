# TalentScout Hiring Assistant 

## Project Overview
The TalentScout Hiring Assistant is a Streamlit-based chatbot designed to assist in the initial screening of candidates for technical roles. The chatbot collects essential candidate information and dynamically generates technical interview questions based on the candidate’s declared tech stack using Large Language Models (LLMs).

## Features
- Interactive chatbot-style interface using Streamlit
- Collects candidate details such as name, email, phone number, experience, desired role, and tech stack
- Generates technical interview questions based on the candidate’s tech stack using OpenAI GPT models
- Asks questions one by one while maintaining conversation context
- Gracefully handles API rate limits using a fallback mechanism
- Ends the conversation with a clear summary and next steps

## Technologies Used
- Python
- Streamlit
- OpenAI GPT (LLM)

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd talentscout-hiring-assistant