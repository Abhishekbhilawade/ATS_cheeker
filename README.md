
# 📄 Advanced ATS Resume Checker

An intelligent resume analysis application built using **Python, Streamlit, and Machine Learning**. It helps job seekers evaluate their resumes against different IT job roles, identify skill gaps, discover relevant keywords, and improve their resumes.

## 🚀 Project Overview

The Advanced ATS Resume Checker analyzes an uploaded resume against a selected job role and generates an estimated ATS compatibility score.

Users can upload PDF or DOCX resumes, select from 40+ IT job roles, and receive personalized analysis and recommendations.

## ✨ Features

- 📄 Upload resumes in PDF and DOCX formats.
- 👀 Preview uploaded resumes.
- 💼 Support for 40+ IT job roles.
- 📊 Estimated ATS compatibility score.
- ✅ Matched skills identification.
- ❌ Missing skills identification.
- 🎯 Skill gap analysis.
- 💡 Relevant keyword suggestions.
- 📝 Resume improvement tips.
- 📈 Text similarity analysis using TF-IDF and Cosine Similarity.

## 💼 Supported Job Roles

### Software Development
- Python Developer
- Java Developer
- Frontend Developer
- Backend Developer
- Full Stack Developer
- Software Engineer
- C++ Developer
- C# Developer
- PHP Developer
- Go Developer
- Ruby Developer

### Data Science and Artificial Intelligence
- Data Analyst
- Data Scientist
- Data Engineer
- Business Analyst
- Machine Learning Engineer
- AI Engineer
- NLP Engineer
- Computer Vision Engineer
- Generative AI Engineer

### Cloud and DevOps
- DevOps Engineer
- Cloud Engineer
- AWS Cloud Engineer
- Azure Cloud Engineer
- Site Reliability Engineer

### Cybersecurity and Networking
- Cybersecurity Analyst
- Ethical Hacker
- Network Engineer
- System Administrator

### Database and Testing
- Database Administrator
- SQL Developer
- QA Engineer
- Automation Test Engineer
- Performance Test Engineer

### Mobile and Design
- Mobile App Developer
- Android Developer
- iOS Developer
- Flutter Developer
- UI/UX Designer
- Product Designer

### Other Technical Roles
- Blockchain Developer
- Embedded Systems Engineer
- Game Developer
- Technical Support Engineer
- IT Support Engineer

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- PyPDF
- Python-docx
- TF-IDF Vectorization
- Cosine Similarity
- Git and GitHub

## 📁 Project Structure

```text
ATS-Resume-Checker/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── utils/
│   ├── __init__.py
│   ├── resume_parser.py
│   └── ats_analyzer.py
│
└── venv/
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Abhishekbhilawade/ATS_cheeker.git
```

### 2. Navigate to the project directory

```bash
cd ATS_cheeker
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
pip install "streamlit[pdf]"
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your web browser.

## 📊 ATS Score Calculation

The application calculates an estimated resume match score using two components.

### 1. Skill Matching Score – 70%

Measures the percentage of required role skills detected in the resume.

### 2. Text Similarity Score – 30%

Uses TF-IDF vectorization and Cosine Similarity to compare the resume content with the selected role description.

### Final Score Formula

```text
ATS Score =
(Skill Matching Score × 0.70)
+
(Text Similarity Score × 0.30)
```

## 🎯 Skill Gap Analysis

The application identifies:

- Skills already present in the resume.
- Skills missing for the selected role.
- Relevant keywords that may be included when supported by genuine experience.
- Areas where the resume could be improved.

## 🔮 Future Improvements

- Generate downloadable PDF analysis reports.
- Add advanced NLP-based resume analysis.
- Add resume section detection.
- Improve keyword recommendations.
- Compare one resume against multiple job roles.
- Add more job categories and skills.
- Deploy the application online.

## ⚠️ Disclaimer

This project provides an educational estimate of resume compatibility. It is not an official ATS system and does not guarantee job selection.

Users should include only skills and experience they genuinely possess.

## 👨‍💻 Author

**Abhishek Bhilawade**

GitHub: [Abhishekbhilawade](https://github.com/Abhishekbhilawade)

Project: [ATS Resume Checker](https://github.com/Abhishekbhilawade/ATS_cheeker)

---

⭐ If you find this project useful, consider giving it a star!
