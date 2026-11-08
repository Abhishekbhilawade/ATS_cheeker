
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# --------------------------------------------------
# JOB ROLES AND REQUIRED SKILLS
# --------------------------------------------------

JOB_ROLES = {
    "Python Developer": [
        "python", "django", "flask", "sql", "rest api",
        "git", "github", "oop", "debugging", "testing"
    ],

    "Java Developer": [
        "java", "spring boot", "hibernate", "sql",
        "rest api", "git", "maven", "microservices",
        "junit", "oop"
    ],

    "Frontend Developer": [
        "html", "css", "javascript", "react", "angular",
        "bootstrap", "responsive design", "git",
        "typescript", "ui design"
    ],

    "Backend Developer": [
        "python", "java", "node.js", "sql", "mongodb",
        "rest api", "authentication", "api development",
        "git", "database"
    ],

    "Full Stack Developer": [
        "html", "css", "javascript", "react", "node.js",
        "express", "mongodb", "sql", "rest api", "git"
    ],

    "Software Engineer": [
        "python", "java", "data structures", "algorithms",
        "oop", "sql", "git", "testing", "debugging",
        "software development"
    ],

    "C++ Developer": [
        "c++", "oop", "data structures", "algorithms",
        "stl", "pointers", "memory management", "git"
    ],

    "C# Developer": [
        "c#", ".net", "asp.net", "sql", "oop",
        "entity framework", "rest api", "git"
    ],

    "PHP Developer": [
        "php", "laravel", "mysql", "html", "css",
        "javascript", "rest api", "git"
    ],

    "Go Developer": [
        "golang", "go", "microservices", "rest api",
        "concurrency", "docker", "sql", "git"
    ],

    "Ruby Developer": [
        "ruby", "ruby on rails", "sql", "rest api",
        "html", "css", "javascript", "git"
    ],

    "Data Analyst": [
        "python", "sql", "excel", "power bi", "tableau",
        "statistics", "data analysis", "data visualization",
        "pandas", "numpy"
    ],

    "Data Scientist": [
        "python", "sql", "machine learning", "statistics",
        "pandas", "numpy", "scikit-learn", "data analysis",
        "data visualization", "deep learning"
    ],

    "Data Engineer": [
        "python", "sql", "spark", "hadoop", "etl",
        "data pipelines", "airflow", "aws",
        "data warehousing", "database"
    ],

    "Business Analyst": [
        "business analysis", "sql", "excel", "power bi",
        "tableau", "requirements gathering", "documentation",
        "data analysis", "communication"
    ],

    "Machine Learning Engineer": [
        "python", "machine learning", "deep learning",
        "tensorflow", "pytorch", "scikit-learn",
        "pandas", "numpy", "statistics", "data preprocessing"
    ],

    "AI Engineer": [
        "python", "artificial intelligence", "machine learning",
        "deep learning", "llm", "nlp", "tensorflow",
        "pytorch", "generative ai", "prompt engineering"
    ],

    "NLP Engineer": [
        "python", "nlp", "natural language processing",
        "transformers", "bert", "llm", "machine learning",
        "deep learning", "pytorch"
    ],

    "Computer Vision Engineer": [
        "python", "computer vision", "opencv",
        "deep learning", "tensorflow", "pytorch",
        "image processing", "cnn"
    ],

    "Generative AI Engineer": [
        "python", "generative ai", "llm",
        "prompt engineering", "rag", "langchain",
        "vector database", "embeddings", "transformers"
    ],

    "DevOps Engineer": [
        "linux", "docker", "kubernetes", "aws",
        "jenkins", "git", "ci/cd", "terraform",
        "python", "bash"
    ],

    "Cloud Engineer": [
        "aws", "azure", "google cloud", "linux",
        "docker", "kubernetes", "networking",
        "terraform", "cloud computing"
    ],

    "AWS Cloud Engineer": [
        "aws", "ec2", "s3", "lambda", "iam",
        "vpc", "cloudwatch", "terraform", "docker"
    ],

    "Azure Cloud Engineer": [
        "azure", "azure devops", "virtual machines",
        "azure functions", "active directory",
        "cloud computing", "terraform", "networking"
    ],

    "Site Reliability Engineer": [
        "linux", "python", "monitoring", "prometheus",
        "grafana", "kubernetes", "docker", "automation",
        "incident management", "cloud"
    ],

    "Cybersecurity Analyst": [
        "network security", "cybersecurity", "penetration testing",
        "vulnerability assessment", "linux", "firewalls",
        "siem", "incident response", "encryption"
    ],

    "Ethical Hacker": [
        "penetration testing", "kali linux", "nmap",
        "metasploit", "burp suite", "network security",
        "vulnerability assessment", "web security"
    ],

    "Network Engineer": [
        "networking", "tcp/ip", "routing", "switching",
        "cisco", "firewalls", "dns", "dhcp", "vpn", "linux"
    ],

    "System Administrator": [
        "linux", "windows server", "system administration",
        "networking", "active directory", "bash",
        "powershell", "backup", "troubleshooting"
    ],

    "Database Administrator": [
        "sql", "mysql", "postgresql", "oracle",
        "database administration", "backup", "performance tuning",
        "database security", "database optimization"
    ],

    "SQL Developer": [
        "sql", "mysql", "postgresql", "oracle",
        "stored procedures", "triggers", "joins",
        "query optimization", "database design"
    ],

    "QA Engineer": [
        "manual testing", "automation testing", "selenium",
        "python", "java", "test cases", "bug tracking",
        "jira", "api testing"
    ],

    "Automation Test Engineer": [
        "selenium", "python", "java", "automation testing",
        "pytest", "testng", "api testing", "cypress",
        "test cases", "jenkins"
    ],

    "Performance Test Engineer": [
        "performance testing", "jmeter", "load testing",
        "stress testing", "monitoring", "api testing",
        "performance analysis"
    ],

    "Mobile App Developer": [
        "android", "kotlin", "java", "swift",
        "flutter", "dart", "react native",
        "mobile development", "rest api"
    ],

    "Android Developer": [
        "android", "kotlin", "java", "android studio",
        "jetpack compose", "firebase", "rest api"
    ],

    "iOS Developer": [
        "swift", "ios", "xcode", "swiftui",
        "uikit", "api integration", "mobile development"
    ],

    "Flutter Developer": [
        "flutter", "dart", "firebase", "rest api",
        "mobile development", "state management",
        "android", "ios"
    ],

    "UI/UX Designer": [
        "figma", "wireframing", "prototyping",
        "user research", "user experience",
        "user interface", "adobe xd", "design systems"
    ],

    "Product Designer": [
        "figma", "user research", "wireframing",
        "prototyping", "design thinking",
        "user experience", "design systems"
    ],

    "Blockchain Developer": [
        "blockchain", "solidity", "ethereum",
        "smart contracts", "web3", "javascript",
        "cryptography", "truffle"
    ],

    "Embedded Systems Engineer": [
        "c", "c++", "embedded systems", "microcontrollers",
        "rtos", "linux", "firmware", "uart", "spi", "i2c"
    ],

    "Game Developer": [
        "c++", "c#", "unity", "unreal engine",
        "game development", "3d graphics",
        "physics", "game programming"
    ],

    "Technical Support Engineer": [
        "troubleshooting", "linux", "windows",
        "networking", "technical support",
        "customer support", "sql", "communication"
    ],

    "IT Support Engineer": [
        "windows", "linux", "networking",
        "hardware troubleshooting", "software installation",
        "active directory", "technical support"
    ]
}


# --------------------------------------------------
# ROLE DESCRIPTIONS
# --------------------------------------------------

ROLE_DESCRIPTIONS = {
    role: " ".join(skills)
    for role, skills in JOB_ROLES.items()
}


# --------------------------------------------------
# TEXT CLEANING
# --------------------------------------------------

def clean_text(text):
    return re.sub(r"\s+", " ", text.lower()).strip()


# --------------------------------------------------
# SKILL DETECTION
# --------------------------------------------------

def find_skills(text, skill_list):

    text = clean_text(text)
    found_skills = []

    for skill in skill_list:

        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


# --------------------------------------------------
# KEYWORD SUGGESTIONS
# --------------------------------------------------

def generate_keyword_suggestions(missing_skills):

    suggestions = []

    for skill in missing_skills:
        suggestions.append(
            f"Consider including '{skill}' if you have relevant experience."
        )

    return suggestions


# --------------------------------------------------
# RESUME IMPROVEMENT TIPS
# --------------------------------------------------

def generate_resume_tips(
    resume_text,
    matched_skills,
    missing_skills
):

    tips = []

    text = clean_text(resume_text)

    if len(text.split()) < 100:
        tips.append(
            "Your resume contains limited text. Add relevant "
            "education, projects, skills, and experience."
        )

    if not any(word in text for word in ["project", "projects"]):
        tips.append(
            "Add a Projects section describing your practical work."
        )

    if not any(word in text for word in ["education", "degree"]):
        tips.append(
            "Consider adding an Education section."
        )

    if not any(word in text for word in ["experience", "internship"]):
        tips.append(
            "Add relevant professional experience or internships, "
            "if applicable."
        )

    if missing_skills:
        tips.append(
            "Develop and demonstrate relevant missing skills "
            "through genuine projects or experience."
        )

    if matched_skills:
        tips.append(
            "Highlight your strongest matching skills near the "
            "top of your resume."
        )

    if not tips:
        tips.append(
            "Your resume has a good basic structure. "
            "Continue tailoring it to the selected job role."
        )

    return tips


# --------------------------------------------------
# ATS RESUME ANALYSIS
# --------------------------------------------------

def analyze_resume(resume_text, selected_role):

    if selected_role not in JOB_ROLES:
        raise ValueError("Please select a valid job role.")

    resume = clean_text(resume_text)

    if not resume:
        raise ValueError("Resume text is empty.")

    required_skills = JOB_ROLES[selected_role]

    role_description = ROLE_DESCRIPTIONS[selected_role]

    matched_skills = find_skills(
        resume,
        required_skills
    )

    missing_skills = [
        skill
        for skill in required_skills
        if skill not in matched_skills
    ]

    skill_score = (
        len(matched_skills) / len(required_skills)
    ) * 100

    try:

        vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2)
        )

        matrix = vectorizer.fit_transform(
            [resume, role_description]
        )

        similarity = cosine_similarity(
            matrix[0:1],
            matrix[1:2]
        )[0][0]

        similarity_score = similarity * 100

    except ValueError:

        similarity_score = 0

    final_score = (
        skill_score * 0.7
    ) + (
        similarity_score * 0.3
    )

    keyword_suggestions = generate_keyword_suggestions(
        missing_skills
    )

    improvement_tips = generate_resume_tips(
        resume,
        matched_skills,
        missing_skills
    )

    return {
        "role": selected_role,
        "score": round(final_score, 2),
        "skill_score": round(skill_score, 2),
        "similarity": round(similarity_score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "required_skills": required_skills,
        "keyword_suggestions": keyword_suggestions,
        "improvement_tips": improvement_tips
    }
