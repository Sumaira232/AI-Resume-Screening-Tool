import streamlit as st
import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------- CONFIG ----------------------
st.set_page_config(page_title="AI Resume Screener", page_icon="📄", layout="centered")

# ---------------------- FUNCTIONS ----------------------
def extract_text(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

def calculate_similarity(job_desc, resume_text):
    text_data = [job_desc, resume_text]
    cv = CountVectorizer().fit_transform(text_data)
    return cosine_similarity(cv)[0][1]

# ---------------------- UI ----------------------
st.title("📄 AI Resume Screening Tool")
st.markdown("Upload your resume and check how well it matches the job description 💼")

# Job Description input (NEW FEATURE)
job_desc = st.text_area("📌 Paste Job Description Here")

# File Upload
uploaded_file = st.file_uploader("📤 Upload Resume (PDF)", type="pdf")

# ---------------------- PROCESS ----------------------
if st.button("Analyze Resume 🚀"):
    if not job_desc:
        st.warning("⚠️ Please enter job description first")
    elif not uploaded_file:
        st.warning("⚠️ Please upload resume")
    else:
        with st.spinner("Analyzing... ⏳"):
            resume_text = extract_text(uploaded_file)
            similarity = calculate_similarity(job_desc, resume_text)
            score = round(similarity * 100, 2)

        # ---------------------- RESULTS ----------------------
        st.subheader("📊 Match Score")
        st.progress(int(score))
        st.write(f"### {score}% Match")

        # Decision
        if similarity > 0.6:
            st.success("✅ Strong Match! Candidate is suitable")
        elif similarity > 0.4:
            st.info("⚡Matched but (Consider improving resume)")
        else:
            st.error("❌ Low Match - Not suitable")

        # ---------------------- EXTRA FEATURE ----------------------
        st.subheader("💡 Tips to Improve Resume")
        if similarity < 0.6:
            st.write("- Add relevant skills from job description")
            st.write("- Use keywords matching the job")
            st.write("- Improve experience section")
        else:
            st.write("Great job! Your resume is well aligned 🎉")