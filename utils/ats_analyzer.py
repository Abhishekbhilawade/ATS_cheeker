
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Job roles and their required skills

JOB_ROLES = {

    "Python Developer": [
        "python",
        "django",
        "flask",
        "sql",
        "rest api",
        "git",
        "github",
        "oop",
        "debugging",
        "testing"
    ],

    "Java Developer": [
        "java",
        "spring boot",
        "hibernate",
        "sql",
        "rest api",
        "git",
        "maven",
        "oops",
        "microservices",
        "junit"
    ],

    "Data Analyst": [
        "python",
        "sql",
        "excel",
        "power bi",
        "tableau",
        "statistics",
        "data analysis",
        "data visualization",
        "pandas",
        "numpy"
    ],

    "Frontend Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "angular",
        "bootstrap",
        "responsive design",
        "git",
        "typescript",
        "ui design"
    ],

    "Full Stack Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "node.js",
        "express",
        "mongodb",
        "sql",
        "rest api",
        "git"
    ],

    "Machine Learning Engineer": [
        "python",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "scikit-learn",
        "pandas",
        "numpy",
        "statistics",
        "data preprocessing"
    ],

    "DevOps Engineer": [
        "linux",
        "docker",
        "kubernetes",
        "aws",
        "jenkins",
        "git",
        "ci/cd",
        "terraform",
        "python",
        "bash"
    ]
}


# Role descriptions for text similarity

ROLE_DESCRIPTIONS = {

    "Python Developer":
        "Python programming backend development Django Flask SQL "
        "REST API object oriented programming testing debugging Git",

    "Java Developer":
        "Java programming Spring Boot Hibernate SQL REST API "
        "microservices Maven software development testing",

    "Data Analyst":
        "Data analysis Python SQL Excel Power BI Tableau statistics "
        "data visualization Pandas NumPy",

    "Frontend Developer":
        "Frontend development HTML CSS JavaScript React Angular "
        "responsive design user interface web development",

    "Full Stack Developer":
        "Full stack web development HTML CSS JavaScript React "
        "Node.js Express MongoDB SQL REST API",

    "Machine Learning Engineer":
        "Machine learning Python deep learning TensorFlow PyTorch "
        "Scikit-learn statistics data preprocessing",

    "DevOps Engineer":
        "DevOps Linux Docker Kubernetes AWS Jenkins Git "
        "continuous integration deployment Terraform scripting"
}


def clean_text(text):

    return re.sub(r"\s+", " ", text.lower()).strip()


def find_skills(text, skill_list):

    text = clean_text(text)

    found_skills = []

    for skill in skill_list:

        pattern = (
            r"(?<!\w)"
            + re.escape(skill.lower())
            + r"(?!\w)"
        )

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


def analyze_resume(resume_text, selected_role):

    resume = clean_text(resume_text)

    required_skills = JOB_ROLES[selected_role]

    role_description = ROLE_DESCRIPTIONS[selected_role]

    # Find skills in resume

    matched_skills = find_skills(
        resume,
        required_skills
    )

    missing_skills = [
        skill for skill in required_skills
        if skill not in matched_skills
    ]

    # Calculate skill matching percentage

    skill_score = (
        len(matched_skills) / len(required_skills)
    ) * 100

    # Calculate text similarity

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    matrix = vectorizer.fit_transform([
        resume,
        role_description
    ])

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )[0][0]

    similarity_score = similarity * 100

    # Calculate final ATS score

    final_score = (
        (skill_score * 0.7) +
        (similarity_score * 0.3)
    )

    return {

        "role": selected_role,

        "score": round(final_score, 2),

        "skill_score": round(skill_score, 2),

        "similarity": round(similarity_score, 2),

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "required_skills": required_skills

    }
