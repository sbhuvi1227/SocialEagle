import streamlit as st
from datetime import date

st.set_page_config(page_title="Job Registration", layout="centered")

# ---------------- CSS Styling ----------------
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to right, #0f3057, #1f6f8b);
            color: white;
        }

        label, h1, h2, h3, p {
            color: white !important;
        }

        /* Gender radio text white */
        div[role="radiogroup"] label span {
            color: white !important;
            font-weight: 600;
        }

        /* Input fields */
        input, textarea {
            background-color: #f0f8ff !important;
            color: black !important;
        }

        /* Select & multiselect text */
        .stSelectbox div, .stMultiSelect div {
            color: black !important;
        }

        /* Submit button inside form */
        div.stForm button {
            background-color: #1f6f8b !important;
            color: black !important;
            border-radius: 8px !important;
            height: 45px !important;
            width: 230px !important;
            font-size: 16px !important;
            font-weight: 700 !important;
            border: none !important;
        }

        div.stForm button:hover {
            background-color: #144d6e !important;
            color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- Header ----------------
st.markdown("""
## 🌟 ABC Technologies
### *Empowering Careers, Building Futures*
---
""")

st.title("📝 Job Opportunity Registration Form")

# ---------------- Form ----------------
with st.form("job_form"):

    full_name = st.text_input("Full Name *")
    email = st.text_input("Email Address *")
    phone = st.text_input("Phone Number *")

    gender = st.radio("Gender", ["Male", "Female", "Other"])

    dob = st.date_input("Date of Birth *",
                        min_value=date(1960, 1, 1),
                        max_value=date.today())

    # ---- Added Heading ----
    st.markdown("### 🎓 Choose Degree")

    qualification = st.selectbox(
        "Highest Qualification *",
        ["Select", "Diploma", "Bachelors", "Masters", "PhD"]
    )

    skills = st.text_area("Key Skills *")

    experience = st.slider("Years of Experience *", 0, 30, 0)

    locations = st.multiselect(
        "Preferred Job Locations *",
        ["Chennai", "Bangalore", "Coimbatore", "Hyderabad", "Mumbai"]
    )

    submit = st.form_submit_button("Submit Application")

# ---------------- Validation ----------------
if submit:
    if (
        not full_name.strip()
        or not email.strip()
        or not phone.strip()
        or not skills.strip()
        or qualification == "Select"
        or not locations
    ):
        st.warning("⚠️ All mandatory fields must be entered before submitting the form!")
    else:
        st.success("✅ Application Submitted Successfully!")
        st.balloons()
