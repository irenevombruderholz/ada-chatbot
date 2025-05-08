import streamlit as st

st.set_page_config(page_title="Ada - Adverse Event Reporter", page_icon="💊")

st.title("🤖 Ada – Report a Side Effect")

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'data' not in st.session_state:
    st.session_state.data = {}

# Step-by-step question flow
def ask_question(prompt, key, input_type="text", options=None):
    st.write(f"Ada 🤖: {prompt}")
    if input_type == "text":
        return st.text_input("You:", key=key)
    elif input_type == "select":
        return st.selectbox("You:", options, key=key)
    elif input_type == "date":
        return st.date_input("You:", key=key)
    elif input_type == "radio":
        return st.radio("You:", options, key=key)
    elif input_type == "textarea":
        return st.text_area("You:", key=key)

# Define question flow
questions = [
    {"prompt": "What is your date of birth?", "key": "dob", "type": "date"},
    {"prompt": "What is your gender?", "key": "gender", "type": "select", "options": ["Male", "Female", "Other", "Prefer not to say"]},
    {"prompt": "What is the name of the medication or product?", "key": "product", "type": "text"},
    # add more steps here...
]

if st.session_state.step < len(questions):
    q = questions[st.session_state.step]
    user_response = ask_question(q["prompt"], q["key"], q.get("type", "text"), q.get("options"))

    if user_response:
        st.session_state.data[q["key"]] = user_response
        st.session_state.step += 1
        st.experimental_rerun()
else:
    st.success("✅ Thank you! Here is a summary of your report:")
    st.write(st.session_state.data)
