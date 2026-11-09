import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Future Study Advisor",
    page_icon="🎓",
    layout="centered"
)

# Career Data
career_data = {
    "Technology & Coding": [
        "BCA",
        "B.Tech Computer Science",
        "B.Sc Computer Science",
        "Software Developer",
        "Web Developer"
    ],

    "Medical & Healthcare": [
        "MBBS",
        "BDS",
        "B.Sc Nursing",
        "Pharmacy",
        "Physiotherapy"
    ],

    "Business & Finance": [
        "B.Com",
        "BBA",
        "Chartered Accountant (CA)",
        "Company Secretary (CS)",
        "Banking"
    ],

    "Government Jobs": [
        "SSC CGL",
        "SSC CHSL",
        "UPSC",
        "Banking Exams",
        "Railway Exams",
        "NDA"
    ],

    "Arts & Creativity": [
        "Graphic Designing",
        "Animation",
        "Fashion Designing",
        "Journalism",
        "Hotel Management"
    ],

    "Law": [
        "BA LLB",
        "BBA LLB",
        "LLB",
        "Legal Studies"
    ]
}

# Custom Styling
st.markdown("""
<style>
.stApp {
    background-color: #eaf2f8;
}

h1 {
    color: #154360;
    text-align: center;
}

.stButton button {
    background-color: #2471a3;
    color: white;
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Heading
st.title("🎓 FUTURE STUDY ADVISOR")

st.markdown(
    "<h4 style='text-align:center;'>"
    "Find the right course and career for your future!"
    "</h4>",
    unsafe_allow_html=True
)

st.divider()

# Student Information
st.header("📚 Student Information")

student_class = st.selectbox(
    "Select Your Class:",
    [
        "Select Class",
        "Class 8",
        "Class 9",
        "Class 10",
        "Class 11",
        "Class 12",
        "After 12th",
        "College Student"
    ]
)

subject = st.selectbox(
    "Favourite Subject:",
    [
        "Select Subject",
        "Mathematics",
        "Science",
        "Biology",
        "Commerce",
        "English",
        "Computer Science",
        "Arts"
    ]
)

interest = st.selectbox(
    "Your Interest:",
    ["Select Interest"] + list(career_data.keys())
)

goal = st.selectbox(
    "Your Goal:",
    [
        "Select Goal",
        "Government Job",
        "Private Job",
        "Business",
        "Higher Studies",
        "Not Decided"
    ]
)

st.divider()

# Buttons
col1, col2 = st.columns(2)

with col1:
    get_future = st.button(
        "🚀 GET MY FUTURE",
        use_container_width=True
    )

with col2:
    reset = st.button(
        "🔄 RESET",
        use_container_width=True
    )

# Reset
if reset:
    st.rerun()

# Generate Advice
if get_future:

    if (
        student_class == "Select Class"
        or subject == "Select Subject"
        or interest == "Select Interest"
        or goal == "Select Goal"
    ):

        st.warning("Please fill in all four options!")

    else:

        courses = career_data[interest]

        st.success("Your Future Study Report is Ready!")

        st.header("📋 YOUR FUTURE STUDY REPORT")

        st.write("**Your Class:**", student_class)
        st.write("**Favourite Subject:**", subject)
        st.write("**Your Interest:**", interest)
        st.write("**Your Goal:**", goal)

        st.divider()

        st.subheader("🎯 RECOMMENDED COURSES")

        for course in courses:
            st.write("✅", course)

        st.divider()

        st.subheader("📖 YOUR NEXT STEPS")

        steps = [
            "Focus on your favourite subjects.",
            "Research the recommended courses.",
            "Check college admission requirements.",
            "Improve your communication skills.",
            "Learn useful computer skills.",
            "Discuss your options with teachers or a career counsellor."
        ]

        for i, step in enumerate(steps, 1):
            st.write(f"{i}. {step}")

        st.divider()

        st.subheader("💡 CAREER ADVICE")

        st.info(
            "Your interest is a good starting point. "
            "Explore different courses before making "
            "your final career decision."
        )

        st.caption(
            "Check official eligibility requirements before applying."
        )

st.divider()

st.caption(
    "Future Study Advisor | Created by Anmol Verma 🎓"
)