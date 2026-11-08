
import streamlit as st

from utils.resume_parser import extract_resume_text
from utils.ats_analyzer import analyze_resume, JOB_ROLES


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Advanced ATS Resume Checker",
    page_icon="📄",
    layout="wide"
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "result" not in st.session_state:
    st.session_state.result = None

if "resume_text" not in st.session_state:
    st.session_state.resume_text = None

if "uploaded_file_name" not in st.session_state:
    st.session_state.uploaded_file_name = None


# --------------------------------------------------
# APPLICATION HEADER
# --------------------------------------------------

st.title("📄 Advanced ATS Resume Checker")

st.markdown(
    "Analyze your resume against 40+ IT job roles, "
    "identify skill gaps, and get suggestions to improve it."
)

st.divider()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("⚙️ Resume Settings")

selected_role = st.sidebar.selectbox(
    "Select your target job role",
    options=list(JOB_ROLES.keys())
)

st.sidebar.info(
    "Choose the job role you want to target. "
    "The application will compare your resume with "
    "the selected role's skills."
)


# --------------------------------------------------
# RESUME UPLOAD
# --------------------------------------------------

st.header("1. Upload Your Resume")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF or DOCX)",
    type=["pdf", "docx"]
)


# --------------------------------------------------
# EXTRACT RESUME TEXT
# --------------------------------------------------

if uploaded_file is not None:

    if st.session_state.uploaded_file_name != uploaded_file.name:

        st.session_state.result = None
        st.session_state.resume_text = None

        st.session_state.uploaded_file_name = uploaded_file.name

    try:

        resume_text = extract_resume_text(uploaded_file)

        st.session_state.resume_text = resume_text

        if not resume_text.strip():

            st.warning(
                "No readable text found. "
                "If this is a scanned PDF, OCR may be required."
            )

    except Exception as error:

        st.error(f"Resume extraction failed: {error}")

        st.session_state.resume_text = None

else:

    st.session_state.resume_text = None
    st.session_state.result = None
    st.session_state.uploaded_file_name = None


# --------------------------------------------------
# RESUME PREVIEW
# --------------------------------------------------

st.divider()

st.header("2. Resume Preview")

left_col, right_col = st.columns(2, gap="large")


with left_col:

    st.subheader("Uploaded Resume")

    if uploaded_file is not None:

        st.success(f"Uploaded: {uploaded_file.name}")

        if st.session_state.resume_text:

            st.metric(
                "Extracted Characters",
                len(st.session_state.resume_text)
            )

    else:

        st.info("Upload your resume to continue.")


with right_col:

    st.subheader("CV Preview")

    if uploaded_file is not None:

        if uploaded_file.name.lower().endswith(".pdf"):

            try:

                st.pdf(
                    uploaded_file.getvalue(),
                    height=600
                )

            except Exception as error:

                st.error(f"PDF preview error: {error}")

        else:

            if st.session_state.resume_text:

                st.text_area(
                    "Resume Content",
                    value=st.session_state.resume_text,
                    height=500,
                    disabled=True
                )

    else:

        st.info("Your resume preview will appear here.")


# --------------------------------------------------
# ANALYZE RESUME
# --------------------------------------------------

st.divider()

st.header("3. Analyze Your Resume")

if uploaded_file is not None and st.session_state.resume_text:

    if st.button(
        "🔍 Analyze Resume",
        type="primary",
        use_container_width=True
    ):

        try:

            with st.spinner("Analyzing your resume..."):

                st.session_state.result = analyze_resume(
                    st.session_state.resume_text,
                    selected_role
                )

        except Exception as error:

            st.error(f"Analysis failed: {error}")


else:

    st.info("Please upload a resume with readable text.")


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

if st.session_state.result is not None:

    result = st.session_state.result

    st.divider()

    st.header("📊 ATS Analysis Results")

    st.write(
        f"**Selected Job Role:** {result['role']}"
    )

    # SCORE CARDS

    score_col, skill_col, similarity_col = st.columns(3)

    with score_col:

        st.metric(
            "Estimated ATS Score",
            f"{result['score']}%"
        )

    with skill_col:

        st.metric(
            "Skill Match",
            f"{result['skill_score']}%"
        )

    with similarity_col:

        st.metric(
            "Text Similarity",
            f"{result['similarity']}%"
        )

    st.subheader("Overall Resume Match")

    st.progress(
        min(max(result["score"] / 100, 0.0), 1.0)
    )

    # MATCHED AND MISSING SKILLS

    st.divider()

    st.header("4. Skill Gap Analysis")

    matched_col, missing_col = st.columns(2)

    with matched_col:

        st.subheader("✅ Matched Skills")

        if result["matched_skills"]:

            for skill in result["matched_skills"]:

                st.success(skill)

        else:

            st.info("No matching skills detected.")

    with missing_col:

        st.subheader("❌ Missing Skills")

        if result["missing_skills"]:

            for skill in result["missing_skills"]:

                st.warning(skill)

        else:

            st.success("All listed skills were detected!")

    # KEYWORD SUGGESTIONS

    st.divider()

    st.header("5. Keyword Suggestions")

    st.write(
        "These are relevant skills that you could consider "
        "including if you genuinely have the knowledge or experience."
    )

    if result["keyword_suggestions"]:

        for suggestion in result["keyword_suggestions"]:

            st.info(f"💡 {suggestion}")

    else:

        st.success("No additional keyword suggestions.")

    # RESUME IMPROVEMENT TIPS

    st.divider()

    st.header("6. Resume Improvement Tips")

    for index, tip in enumerate(
        result["improvement_tips"],
        start=1
    ):

        st.write(f"**{index}.** {tip}")

    # REQUIRED SKILLS

    with st.expander("View all required skills for this role"):

        st.write(
            ", ".join(result["required_skills"])
        )

    # DISCLAIMER

    st.divider()

    st.caption(
        "Disclaimer: This application provides an educational "
        "resume-matching estimate, not an official ATS score. "
        "Always include only skills and experience that you genuinely possess."
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Advanced ATS Resume Checker | Python + Streamlit + Scikit-learn"
)
