# 📧 Cold Mail Generator

An AI-powered cold email generation tool built using **Python, Streamlit, LangChain, Groq API, and ChromaDB**.  
This application allows users to input a company careers page URL, automatically extracts job listings, analyzes required skills, and generates highly personalized cold outreach emails for service-based companies.

It also intelligently fetches relevant portfolio/project links from a **vector database** based on the job description, making the generated email more targeted and professional.

---

## 🚀 Key Features

1. 🌐 **Career Page URL Input**  
   Enter any company careers/job posting URL.

2. 🕵️ **Automatic Job Data Extraction**  
   Scrapes and extracts job role, experience, skills, and description.

3. 🤖 **AI-Powered Cold Email Writing**  
   Generates personalized cold emails using Groq LLM.

4. 🔗 **Portfolio Link Matching**  
   Uses ChromaDB vector search to fetch relevant portfolio links based on skills.

5. 🎯 **Highly Targeted Outreach Emails**  
   Customized emails aligned to company requirements.

6. ⚡ **Fast Streamlit Interface**  
   Clean and responsive UI for instant generation.

7. 🧠 **LangChain Pipeline Integration**  
   Prompt templates + output parsing + chains.

8. 💾 **Persistent Vector Store**  
   Portfolio embeddings stored locally for reuse.

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
│   └── utils.py
│
│── vectorstore/
│── email-generator.ipynb
│── requirements.txt
│── README.md
```

---

## ⚙️ Tech Stack

| Layer      | Technology                     |
|------------|--------------------------------|
| Frontend UI	| Streamlit |
| Backend Logic |	Python |
| LLM Engine |	Groq API (Llama Models) |
| Framework |	LangChain |
| Vector Database |	ChromaDB |
| Data Handling |	Pandas |
| Web Scraping |	WebBaseLoader, BeautifulSoup4 |

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

## 📍 Example Workflow

- Open the Streamlit app.
- Paste a company job posting URL.
- App extracts job description automatically.
- Relevant portfolio links are searched using ChromaDB.
- Personalized cold email gets generated instantly.

---

## 📸 Project Output

<img width="1779" height="886" alt="Cold_Email_Output" src="https://github.com/user-attachments/assets/0e58b666-57e4-436b-8704-942d20c18ef4" />

Example Output Includes:

- ✅ Subject Line
- ✅ Personalized Introduction
- ✅ Relevant Skills Match
- ✅ Portfolio Links
- ✅ Strong CTA

---

## 💡 Example Use Cases

- Freelancers pitching companies
- Agencies sending outreach emails
- Service companies generating leads
- Sales automation projects
- AI portfolio projects for resume

---

## 🔮 Future Improvements

- Multi-email generation
- Gmail sending integration
- PDF export
- Company name auto-detection
- Better UI themes
- Email tone selector

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
