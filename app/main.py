import streamlit as st
import pandas as pd
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text
from email_sender import send_email


# ---------------------------------
# PAGE CONFIG
# ---------------------------------
st.set_page_config(
    page_title="Cold Mail Generator",
    page_icon="📧",
    layout="wide"
)

st.title("📧 Cold Mail Generator")
st.write("Generate personalized cold emails from job URLs.")


# ---------------------------------
# OBJECTS
# ---------------------------------
llm = Chain()
portfolio = Portfolio()


# ---------------------------------
# SESSION STATE
# ---------------------------------
if "generated_data" not in st.session_state:
    st.session_state.generated_data = []


# ---------------------------------
# INPUTS
# ---------------------------------
url_input = st.text_input("Enter Job URL")

uploaded_file = st.file_uploader(
    "Upload CSV with URLs",
    type=["csv"]
)


# ---------------------------------
# GENERATE BUTTON
# ---------------------------------
if st.button("Generate Emails"):

    urls = []

    # Single URL
    if url_input.strip():
        urls.append(url_input.strip())

    # CSV Upload
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)

            if "url" not in df.columns:
                st.error("CSV must contain a column named: url")
                st.stop()

            csv_urls = df["url"].dropna().tolist()
            urls.extend(csv_urls)

        except Exception as e:
            st.error(f"CSV Error: {e}")
            st.stop()

    # No Input
    if not urls:
        st.warning("Please enter URL or upload CSV file.")
        st.stop()

    st.session_state.generated_data = []

    # Load portfolio once
    portfolio.load_portfolio()

    # Process URLs
    for idx, url in enumerate(urls):

        try:
            with st.spinner(f"Processing URL {idx + 1}..."):

                loader = WebBaseLoader([url])
                page_data = loader.load().pop().page_content

                data = clean_text(page_data)

                jobs = llm.extract_jobs(data)

                if isinstance(jobs, dict):
                    jobs = [jobs]

                for j, job in enumerate(jobs):

                    skills = job.get("skills", [])

                    links = portfolio.query_links(skills)

                    email = llm.write_mail(job, links)

                    st.session_state.generated_data.append({
                        "url_no": idx + 1,
                        "job_no": j + 1,
                        "email": email
                    })

        except Exception as e:
            st.error(f"Error processing {url}: {e}")


# ---------------------------------
# DISPLAY GENERATED EMAILS
# ---------------------------------
for item in st.session_state.generated_data:

    url_no = item["url_no"]
    job_no = item["job_no"]
    email = item["email"]

    st.markdown("---")
    st.subheader(f"🔗 Processing URL {url_no}")
    st.markdown(f"### 📌 Job {job_no}")

    st.code(email, language="markdown")

    receiver = st.text_input(
        f"Enter Recipient Email (URL {url_no} Job {job_no})",
        key=f"receiver_{url_no}_{job_no}"
    )

    if st.button(
        f"Send Email {url_no}-{job_no}",
        key=f"send_{url_no}_{job_no}"
    ):

        try:
            if receiver.strip() == "":
                st.warning("Please enter receiver email.")

            else:
                send_email(
                    receiver,
                    "Business Proposal",
                    email
                )

                st.success("✅ Email Sent Successfully!")

        except Exception as e:
            st.error(f"Email failed: {e}")
