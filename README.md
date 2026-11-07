
# 📄 ATS Resume Checker

An intelligent ATS Resume Checker built using Python and Streamlit. This application analyzes resumes against selected job roles and provides an estimated ATS compatibility score.

## 🚀 Project Overview

The ATS Resume Checker helps job seekers understand how well their resumes match a particular job role.

Users can upload their resumes in PDF or DOCX format, select their desired job role, and receive an analysis showing matched skills, missing skills, and an estimated ATS score.

## ✨ Features

- Upload resumes in PDF and DOCX formats.
- Preview uploaded resumes.
- Select from multiple job roles.
- Extract text from resumes automatically.
- Identify matched and missing skills.
- Calculate an estimated ATS compatibility score.
- Display skill matching percentage.
- Calculate text similarity using TF-IDF and cosine similarity.
- Simple and interactive Streamlit interface.

## 🛠️ Technologies Used

- Python
- Streamlit
- PyPDF
- Python-docx
- Scikit-learn
- TF-IDF
- Cosine Similarity

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

### 2. Navigate to the project folder

```bash
cd ATS_cheeker
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

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

The application will open in your browser.

## 📊 How ATS Score Is Calculated

The application uses two main components:

**1. Skill Matching Score (70%)**

Checks how many required skills for the selected job role are present in the resume.

**2. Text Similarity Score (30%)**

Uses TF-IDF vectorization and cosine similarity to compare resume content with the selected role description.

**Final Score:**

```text
ATS Score =
(Skill Matching Score × 0.70)
+
(Text Similarity Score × 0.30)
```

## 🎯 Supported Job Roles

- Python Developer
- Java Developer
- Data Analyst
- Frontend Developer
- Full Stack Developer
- Machine Learning Engineer
- DevOps Engineer

## 🔮 Future Improvements

- Add more job roles.
- Improve skill extraction using NLP.
- Add resume improvement suggestions.
- Provide downloadable analysis reports.
- Add resume section detection.
- Improve keyword recommendations.

## ⚠️ Disclaimer

This project provides an educational estimate of resume compatibility. It is not an official ATS system and does not guarantee selection by recruiters.

## 👨‍💻 Author

**Abhishek Bhilawade**

GitHub: https://github.com/Abhishekbhilawade

---

⭐ If you find this project useful, consider giving it a star!
