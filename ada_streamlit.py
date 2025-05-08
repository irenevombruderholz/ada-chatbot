import streamlit as st

st.set_page_config(page_title="Ada - Adverse Event Reporter", page_icon="💊")

st.title("🤖 Ada – Report a Side Effect")

with st.form("adr_form"):
    dob = st.date_input("What is your date of birth?")
    gender = st.selectbox("What is your gender?", ["Male", "Female", "Other", "Prefer not to say"])
    product = st.text_input("What is the name of the medication or product?")
    intake_date = st.date_input("When did you take the medication?")
    symptoms = st.text_area("What symptoms or side effects did you experience?")
    outcome = st.text_input("What was the outcome of the symptoms?")
    treatment = st.text_input("Did you receive any treatment for the symptoms?")
    hospitalization = st.radio("Were you hospitalized due to the reaction?", ["Yes", "No"])
    other_info = st.text_area("Do you want to share any other relevant information?")
    consent = st.radio("Do you consent to be contacted for further information if needed?", ["Yes", "No"])

    submitted = st.form_submit_button("Submit Report")

if submitted:
    st.success("✅ Thank you! Here is a summary of your report:")
    st.write({
        "Date of Birth": str(dob),
        "Gender": gender,
        "Product": product,
        "Date of Intake": str(intake_date),
        "Symptoms": symptoms,
        "Outcome": outcome,
        "Treatment": treatment,
        "Hospitalization": hospitalization,
        "Other Info": other_info,
        "Consent for Follow-up": consent
    })

