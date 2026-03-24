# 📄 AI Resume Screening Tool (NLP + Streamlit)

🚀 A powerful AI-based Resume Screening Tool that analyzes resumes against job descriptions and provides a match score, keyword insights, and improvement suggestions.

---

## 🎥 Demo Video

👉 Watch the demo here:  
▶️https://www.linkedin.com/posts/sumaira-a-949584342_activity-7442219937676386304-p29n?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFXexEkB8KFKMVtWhd-KbHOZYpDnPJaEJ6w

---

## 📌 Features

- 📤 Upload Resume (PDF format)
- 📌 Paste Job Description
- 📊 Match Score using NLP (Cosine Similarity)
- 📈 Progress Bar Visualization
- 🔑 Keyword Matching & Missing Keywords Detection
- 💡 Smart Resume Improvement Suggestions
- ⚡ Fast and Interactive UI (Streamlit)

---

## 🧠 How It Works

1. Extracts text from the uploaded resume using **PyPDF2**
2. Converts text into vectors using **CountVectorizer**
3. Compares resume with job description using **Cosine Similarity**
4. Generates:
   - Match Score (%)
   - Candidate suitability
   - Improvement suggestions

---

## 🛠 Tech Stack

- Python 🐍
- Streamlit 🎨
- Scikit-learn 🤖
- PyPDF2 📄

---

## 📂 Project Structure

```

AI-Resume-Screening-Tool/
│
├── app.py                # Main Streamlit App
├── requirements.txt     # Dependencies
├── README.md            # Project Documentation
|---resumes/

```

---

## ⚙️ Installation & Setup (Step-by-Step)

### 🔹 Step 1: Clone Repository

```

git clone https://github.com/YOUR_USERNAME/AI-Resume-Screening-Tool.git

```

### 🔹 Step 2: Go to Project Folder

```

cd AI-Resume-Screening-Tool

```

### 🔹 Step 3: Create Virtual Environment

```

python -m venv venv

```

### 🔹 Step 4: Activate Environment

**For Windows:**
```

venv\Scripts\activate

```

**For Mac/Linux:**
```

source venv/bin/activate

```

---

### 🔹 Step 5: Install Requirements

```

pip install -r requirements.txt

```

---

### 🔹 Step 6: Run the Application

```

streamlit run app.py

```

---

## 🚀 How to Use

1. Open the app in browser  
2. Paste Job Description  
3. Upload your Resume (PDF)  
4. Click **"Analyze Resume"**  
5. View:
   - Match Score
   - Candidate Status
   - Improvement Suggestions  

---

## 📊 Example Output

- Match Score: **75%**
- Status: ✅ Suitable Candidate
- Suggestions:
  - Add more relevant keywords
  - Improve experience section
  - Match skills with job description

---

## 💡 Future Improvements

- Multiple resume comparison
- Resume editing inside app
- AI-based resume rewriting
- Download analysis report (PDF)
- Keyword highlighting inside resume

---

## 🙌 Contribution

Feel free to fork this repository and improve it!

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub!

---

## 👩‍💻 Author

**Sumaira**  
🔗 GitHub: https://github.com/Sumaira232
