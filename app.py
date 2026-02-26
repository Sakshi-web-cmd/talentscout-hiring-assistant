import streamlit as st
from openai import OpenAI, RateLimitError
import os

# ------------------ OPENAI CLIENT ------------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ------------------ TITLE & INTRO ------------------
st.title(" TalentScout Hiring Assistant")

st.write(
    "Hi! Welcome to TalentScout.\n\n"
    "I will collect a few details and then ask technical questions "
    "based on your tech stack as part of the initial screening."
)

# ------------------ SESSION STATE INIT ------------------
fields = ["name", "email", "phone", "experience", "role", "tech_stack"]
for f in fields:
    if f not in st.session_state:
        st.session_state[f] = ""

if "questions" not in st.session_state:
    st.session_state.questions = []

if "q_index" not in st.session_state:
    st.session_state.q_index = 0


# ------------------ LLM QUESTION GENERATOR (REAL + SAFE FALLBACK) ------------------
def generate_questions_llm(tech_stack: str):
    prompt = f"""
You are a technical interviewer.

Generate 3 technical interview questions
for each technology listed below.

Tech Stack:
{tech_stack}

Rules:
- Medium difficulty
- No answers
- One question per line
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert technical interviewer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        text = response.choices[0].message.content

        questions = [
            q.strip("- ").strip()
            for q in text.split("\n")
            if q.strip()
        ]

        # SAFETY: if GPT returns weird format
        if questions:
            return questions

    except RateLimitError:
        pass
    except Exception:
        pass

    # ---- GUARANTEED FALLBACK (NEVER EMPTY) ----
    fallback = []
    for tech in tech_stack.split(","):
        tech = tech.strip()
        if tech:
            fallback.append(f"What is {tech}?")
            fallback.append(f"Explain one important concept in {tech}.")
            fallback.append(f"Describe a real-world use case of {tech}.")
    return fallback


# ------------------ DETAILS COLLECTION ------------------
if st.session_state.name == "":
    name = st.text_input("What is your full name?")
    if st.button("Next") and name:
        st.session_state.name = name
        st.rerun()

elif st.session_state.email == "":
    email = st.text_input("What is your email address?")
    if st.button("Next") and email:
        st.session_state.email = email
        st.rerun()

elif st.session_state.phone == "":
    phone = st.text_input("What is your phone number?")
    if st.button("Next") and phone:
        st.session_state.phone = phone
        st.rerun()

elif st.session_state.experience == "":
    exp = st.text_input("How many years of experience do you have?")
    if st.button("Next") and exp:
        st.session_state.experience = exp
        st.rerun()

elif st.session_state.role == "":
    role = st.text_input("What position are you applying for?")
    if st.button("Next") and role:
        st.session_state.role = role
        st.rerun()

elif st.session_state.tech_stack == "":
    tech = st.text_input(
        "Please list your tech stack (e.g., Python, HTML, SQL)"
    )
    if st.button("Start Technical Questions") and tech:
        st.session_state.tech_stack = tech

        with st.spinner("Generating technical questions..."):
            st.session_state.questions = generate_questions_llm(tech)

        st.session_state.q_index = 0
        st.rerun()


# ------------------ TECHNICAL QUESTIONS (ONE BY ONE) ------------------
elif st.session_state.q_index < len(st.session_state.questions):
    st.write(f"### Technical Question {st.session_state.q_index + 1}")
    st.write(st.session_state.questions[st.session_state.q_index])

    answer = st.text_area("Your answer", key=f"answer_{st.session_state.q_index}")

    if st.button("Next Question"):
        st.session_state.q_index += 1
        st.rerun()


# ------------------ END CONVERSATION ------------------
else:
    st.success(" Initial Screening Completed")

    st.write(
        "Thank you for completing the initial screening.\n\n"
        "Our recruitment team will review your profile and "
        "contact you regarding the next steps."
    )

    st.write("###  Candidate Summary")
    st.write(f" Name: {st.session_state.name}")
    st.write(f" Email: {st.session_state.email}")
    st.write(f" Phone: {st.session_state.phone}")
    st.write(f" Experience: {st.session_state.experience} years")
    st.write(f" Role: {st.session_state.role}")
    st.write(f" Tech Stack: {st.session_state.tech_stack}")