# SmartHireAI - AI-Powered Resume Analyzer and Job Matcher 🚀

SmartHireAI is an advanced AI-based tool that analyzes resumes, scores them against job descriptions, and suggests improvements using GPT-4. Ideal for job seekers and recruiters looking to match the right talent to the right roles.

---

## 🔥 Features
- 🧾 Upload and parse resumes (PDF)
- 📊 BERT-based Job Description Matching
- 🧠 GPT-4-powered Resume Optimization (summaries, bullet points)
- 📈 Skill & Experience Radar Chart
- ☁️ Streamlit Cloud UI (1-click deploy)

---

## 💻 Tech Stack
- **Python 3.10+**
- **Streamlit** for UI
- **Sentence-BERT** for similarity scoring
- **OpenAI GPT-4 API** for resume enhancement
- **Matplotlib / Plotly** for visualizations
- **PyMuPDF** for PDF parsing

---

## 🚀 Installation & Usage

### 🔧 Step 1: Clone and install
```bash
git clone https://github.com/<your-username>/SmartHireAI.git
cd SmartHireAI
pip install -r requirements.txt


🔧 Step 2: Add OpenAI Key
Create a .env file:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_key_here


🔧 Step 3: Run app
bash
Copy
Edit
streamlit run app.py
