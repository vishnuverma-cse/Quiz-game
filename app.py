import streamlit as st

st.set_page_config(page_title="Quiz Game", page_icon="")

questions = [
    {
        "question": "Python kya hai?",
        "options": ["Programming Language", "Browser", "Operating System", "Database"],
        "answer": "Programming Language"
    },
    {
        "question": "HTML ka full form kya hai?",
        "options": [
            "Hyper Text Markup Language",
            "High Text Machine Language",
            "Hyper Tool Multi Language",
            "Home Text Markup Language"
        ],
        "answer": "Hyper Text Markup Language"
    },
    {
        "question": "C++ kis type ki language hai?",
        "options": [
            "Programming Language",
            "Database",
            "Browser",
            "Operating System"
        ],
        "answer": "Programming Language"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "CSS ka use kisliye hota hai?",
        "options": [
            "Website design",
            "Database",
            "Operating System",
            "Compiler"
        ],
        "answer": "Website design"
    }
]

# Session state
if "question_no" not in st.session_state:
    st.session_state.question_no = 0

if "score" not in st.session_state:
    st.session_state.score = 0

st.title(" Quiz Game")
st.write(
    f"Question {st.session_state.question_no + 1} "
    f"of {len(questions)}"
)

# Quiz complete
if st.session_state.question_no >= len(questions):
    st.success(" Quiz Complete!")
    st.subheader(
        f"Your Score: {st.session_state.score}/{len(questions)}"
    )

    if st.button(" Restart Quiz"):
        st.session_state.question_no = 0
        st.session_state.score = 0
        st.rerun()

else:
    current = questions[st.session_state.question_no]

    st.subheader(current["question"])

    selected = st.radio(
        "Choose your answer:",
        current["options"],
        key=f"question_{st.session_state.question_no}"
    )

    if st.button("Next "):
        if selected == current["answer"]:
            st.session_state.score += 1
            st.success("Correct!")

        else:
            st.error(
                f"❌ Wrong! Correct answer: {current['answer']}"
            )

        st.session_state.question_no += 1
        st.rerun()