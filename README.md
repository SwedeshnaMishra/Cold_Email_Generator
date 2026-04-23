# 📧 Cold Mail Generator

An AI-powered cold email automation tool built using **Python, Streamlit, LangChain, Groq API, and ChromaDB**.

Users can enter a single job URL or upload a CSV file containing multiple career page URLs. The application extracts job details, identifies required skills, matches relevant portfolio links using a vector database, generates personalized cold emails, and allows direct Gmail sending using SMTP integration.

---

## 🚀 Key Features

- 🔗 Generate personalized cold emails from a single job URL
- 📂 Bulk cold email generation using CSV upload
- 🤖 AI-powered email generation using Groq LLM
- 🧠 Skill extraction from job descriptions
- 📁 Portfolio link matching using ChromaDB vector search
- 📬 Direct Gmail sending integration
- ⚡ Fast and clean Streamlit web interface
- 🎯 Personalized outreach based on role requirements

---

## 📁 Folder Structure Overview

```bash
Cold-Email-Generator/
│── app/
│   ├── resources/
│   │   └── my_portfolio.csv
│   ├── .env
│   ├── chains.py
│   ├── main.py
│   ├── portfolio.py
│   ├── email_sender.py
│   └── utils.py
│
│── vectorstore/
│── outputs/
│── requirements.txt
│── README.md
```

---

## ⚙️ Tech Stack

| Layer      | Technology                     |
|------------|--------------------------------|
| Frontend | Streamlit |
| Backend | Python |
| LLM | Groq API |
| AI Framework | LangChain |
| Vector Database | ChromaDB |
| Web Scraping | BeautifulSoup4, WebBaseLoader |
| Email Service | Gmail SMTP |

---

## 🛠 Setup Instructions

### Clone Repository

```bash
git clone https://github.com/SwedeshnaMishra/Cold_Email_Generator.git
cd Cold_Email_Generator
```

### Create Virtual Environment

```bash
python -m venv venv
```

*Activate:*

- Windows
```bash
venv\Scripts\activate
```

- Mac/Linux
```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create `.env` File inside app/

```bash
GROQ_API_KEY=your_groq_api_key
EMAIL=yourgmail@gmail.com
EMAIL_PASS=your_google_app_password
```

### Run Streamlit App

```bash
streamlit run app/main.py
```
---

## 🌍 App Runs On

```bash
http://localhost:8501
```

---

## 📂 CSV Format for Bulk Emails

Create a CSV file like this:

```
url
https://careers.nike.com/software-engineer-ii-itc/job/R-77036
https://careers.nike.com/software-engineer-iii-itc/job/R-78696
```

Upload it in the Streamlit UI.

---

## 📸 Project Screenshots

### 🔹 Home Page
<img width="1846" height="484" alt="home" src="https://github.com/user-attachments/assets/ebedd664-8205-4b22-895e-d4fe27a55ea2" />

### 🔹 Bulk Email Generation
<img width="1824" height="810" alt="emailgenerated1" src="https://github.com/user-attachments/assets/2478190d-5cb5-4994-b0a8-fed2b69e4b59" />
<img width="1833" height="670" alt="emilgenerated2" src="https://github.com/user-attachments/assets/277f4914-976f-44c4-a521-0f6515cb1cc1" />

### 🔹 Gmail Sending Integration
<img width="1515" height="799" alt="emailsent" src="https://github.com/user-attachments/assets/d4f532ab-2c9f-4b30-aacf-136171359b35" />

---

## 💼 Real World Use Case

This project helps service companies automate outbound lead generation by converting job postings into personalized cold outreach emails at scale.

---

## 🔥 Highlights

- Reduced manual outreach effort by 80%
- Supports bulk cold email generation using CSV upload
- Integrated direct Gmail delivery through SMTP
- Generates personalized AI-powered outreach emails in seconds
- Matches relevant portfolio links using ChromaDB vector search

---

## 📌 Example Workflow

1. Enter a job URL or upload a CSV file with multiple URLs  
2. Extract job details and required skills automatically  
3. Match relevant portfolio links using vector search  
4. Generate personalized cold emails instantly  
5. Enter recipient email address  
6. Send emails directly through Gmail integration

---

## For Contributing
If you want to contribute to this project, please follow these steps:
- `Fork` the repository.
- Create a new branch `(git checkout -b feature/your-feature-name)`.
- Make your changes and commit them `(git commit -m 'Add some feature')`.
- Push to the branch `(git push origin feature/your-feature-name)`.
- Open a pull request.

---

## Project Maintainer
**Github:** [Swedeshna Mishra](https://github.com/SwedeshnaMishra)
