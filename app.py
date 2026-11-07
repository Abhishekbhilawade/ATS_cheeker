
import streamlit as st

from utils.resume_parser import extract_resume_text
from utils.ats_analyzer import analyze_resume, JOB_ROLES


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="ATS Resume Checker",
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
# APPLICATION TITLE
# --------------------------------------------------

st.title("📄 ATS Resume Checker")

st.write(
    "Upload your resume, select your target job role, "
    "and check how well your resume matches that role."
)

st.divider()


# --------------------------------------------------
# RESUME UPLOAD AND JOB ROLE
# --------------------------------------------------

st.subheader("1. Upload Your Resume")

uploaded_file = st.file_uploader(
    "Choose your resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

selected_role = st.selectbox(
    "Select your target job role",
    options=list(JOB_ROLES.keys())
)


# --------------------------------------------------
# EXTRACT RESUME TEXT
# --------------------------------------------------

if uploaded_file is not None:

    # Reset previous results when a different file is uploaded
    if st.session_state.uploaded_file_name != uploaded_file.name:
        st.session_state.result = None
        st.session_state.resume_text = None
        st.session_state.uploaded_file_name = uploaded_file.name

    try:
        resume_text = extract_resume_text(uploaded_file)

        st.session_state.resume_text = resume_text

        if not resume_text.strip():
            st.warning(
                "No readable text was found in this resume. "
                "If it is a scanned PDF, it may need OCR processing."
            )

    except Exception as error:
        st.error(f"Could not read the resume: {error}")
        st.session_state.resume_text = None

else:
    st.session_state.resume_text = None
    st.session_state.result = None
    st.session_state.uploaded_file_name = None


st.divider()


# --------------------------------------------------
# RESUME PREVIEW
# --------------------------------------------------

st.subheader("2. Resume Preview")

left_col, right_col = st.columns(2, gap="large")


with left_col:

    st.markdown("### Uploaded Resume")

    if uploaded_file is not None:

        st.success(f"Uploaded: {uploaded_file.name}")

        st.caption(
            "Your resume has been uploaded successfully."
        )

        if st.session_state.resume_text:
            st.write(
                f"Extracted text: "
                f"{len(st.session_state.resume_text)} characters"
            )

    else:
        st.info("Upload a PDF or DOCX resume to continue.")


with right_col:

    st.markdown("### CV Preview")

    if uploaded_file is not None:

        if uploaded_file.name.lower().endswith(".pdf"):

            try:
                pdf_bytes = uploaded_file.getvalue()

                st.pdf(
                    pdf_bytes,
                    height=650
                )

            except Exception as error:
                st.error(
                    f"Unable to display PDF preview: {error}"
                )

        elif uploaded_file.name.lower().endswith(".docx"):

            st.info("DOCX Resume Preview")

            if st.session_state.resume_text:

                st.text_area(
                    "Resume Content",
                    value=st.session_state.resume_text,
                    height=500,
                    disabled=True
                )

    else:
        st.info("Your resume preview will appear here.")


st.divider()


# --------------------------------------------------
# RESUME ANALYSIS
# --------------------------------------------------

st.subheader("3. Analyze Your Resume")

if uploaded_file is not None and st.session_state.resume_text:

    if st.button(
        "🔍 Analyze Resume",
        type="primary",
        use_container_width=True
    ):

        try:

            with st.spinner("Analyzing your resume..."):

                result = analyze_resume(
                    st.session_state.resume_text,
                    selected_role
                )

                st.session_state.result = result

        except Exception as error:

            st.error(f"Analysis failed: {error}")

else:

    st.info(
        "Please upload a resume containing readable text "
        "before starting the analysis."
    )


# --------------------------------------------------
# DISPLAY ANALYSIS RESULTS
# --------------------------------------------------

if st.session_state.result is not None:

    result = st.session_state.result

    st.divider()

    st.header("📊 ATS Analysis Results")

    st.write(
        f"**Selected Job Role:** {result['role']}"
    )

    # ATS SCORE
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

    # SCORE PROGRESS BAR
    st.subheader("Overall Resume Match")

    st.progress(
        min(max(result["score"] / 100, 0.0), 1.0)
    )

    if result["score"] >= 75:
        st.success("Good match! Your resume covers many of the selected role's requirements.")

    elif result["score"] >= 50:
        st.warning("Moderate match. Consider improving your resume with relevant skills and experience.")

    else:
        st.error("Low match. Consider adding relevant skills and projects where you have genuine experience.")

    st.divider()

    # MATCHED AND MISSING SKILLS
    matched_col, missing_col = st.columns(2, gap="large")

    with matched_col:

        st.subheader("✅ Matched Skills")

        if result["matched_skills"]:

            for skill in result["matched_skills"]:
                st.success(skill)

        else:
            st.info("No required skills were detected.")

    with missing_col:

        st.subheader("❌ Missing Skills")

        if result["missing_skills"]:

            for skill in result["missing_skills"]:
                st.warning(skill)

        else:
            st.success("All listed role skills were detected!")

    st.divider()

    # ALL REQUIRED SKILLS
    with st.expander("View all required skills"):

        st.write(
            ", ".join(result["required_skills"])
        )

    # DISCLAIMER
    st.caption(
        "Note: This is an educational resume-matching estimate, "
        "not an official ATS score. Results depend on the "
        "skills and role descriptions configured in this project."
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "ATS Resume Checker | Built with Python and Streamlit"
)
