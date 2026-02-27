# TalentScout Hiring Assistant 

## Project Overview
The TalentScout Hiring Assistant is a Streamlit-based chatbot designed to assist in the **initial screening of candidates** for technical roles. The chatbot interactively collects essential candidate information and generates **technology-specific technical interview questions** based on the candidate’s declared tech stack using **Large Language Models (LLMs)**.

This project demonstrates prompt engineering, context-aware conversational flow, and reliable system design with graceful fallback handling.

---

## Features
- Interactive chatbot-style interface built using Streamlit
- Greets candidates and explains the screening process
- Collects essential candidate details:
  - Full Name
  - Email Address
  - Phone Number
  - Years of Experience
  - Desired Position
  - Current Location
  - Tech Stack
- Generates **3–5 technical interview questions** based on the declared tech stack
- Asks technical questions one by one while maintaining conversation context
- Uses LLM-based question generation with a fallback mechanism for reliability
- Displays a clear interview summary at the end
- Gracefully concludes the conversation with next steps

---

## Technologies Used
- **Python**
- **Streamlit** – for building the frontend user interface
- **Large Language Models (LLMs)** – for generating technical interview questions

---


## Installation & Setup
Follow the steps below to run the application locally:



### 1. Clone the repository
```bash
git clone <repository-url>
cd talentscout-hiring-assistant

# Install required libraries
pip install -r requirements.txt

# Set the OpenAI key as an environment variable (Windows PowerShell)
$env:OPENAI_API_KEY="your_api_key_here"

# Run the application
streamlit run app.py

```

## Usage Guide
- Launch the application in the browser.
- The chatbot greets the candidate and explains its purpose.
- Enter candidate details step by step.
- Provide the tech stack (e.g., Python, HTML, SQL).
- The chatbot generates and asks technical questions sequentially.
- Answer the questions and proceed through the interview flow.
- View the interview summary and completion status at the end.

---

## Prompt Design
Prompt engineering is used to guide the LLM to behave as a **technical interviewer**.

The prompts ensure:
- Medium-difficulty questions
- Technology-specific relevance
- No answers included in the output
- Clear and concise questions

This enables effective assessment of the candidate’s technical proficiency during the initial screening.

---

## Context Handling
The application uses Streamlit’s `session_state` to:
- Preserve candidate inputs across steps
- Maintain the sequence of technical questions
- Ensure a smooth and coherent conversational flow

---

## Fallback Mechanism
To ensure reliability, a fallback mechanism is implemented.

If the LLM API is unavailable or quota limits are reached, the chatbot generates structured baseline technical questions. This prevents application crashes and ensures uninterrupted user experience.

---

## Data Privacy
All candidate data is processed only during the active session.

No information is stored permanently or shared externally, ensuring compliance with data privacy best practices.

---

## Challenges & Solutions
**Challenge:** API quota limitations affecting live LLM responses  
**Solution:** Implemented a fallback mechanism to generate technical questions reliably.

**Challenge:** Maintaining conversational flow in a Streamlit application  
**Solution:** Used session-based state management to preserve context across interactions.

---

## Demo Video
A short demo video demonstrating the chatbot’s functionality is available here:  
**Demo Video Link:** [https://drive.google.com/file/d/1g9hMl65IFrJu6Cug5vnXaHTvYKTwCfmx/view?usp=drivesdk](https://drive.google.com/file/d/1Syae1d0DSYUbUkVQAB2LgJzJXH2xKPKV/view)

---

## Future Enhancements
- Automatic evaluation and scoring of candidate responses
- Answer analytics and reporting
- Multilingual support
- Cloud deployment optimizations for scalability
