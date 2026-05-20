import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Text Summarizer")

st.title("🧠 AI Text Summarizer")
st.write("Paste a long text and generate a short summary.")

text = st.text_area("Enter your text", height=250)

summarizer = pipeline("summarization")

if st.button("Generate Summary"):
    if text:
        summary = summarizer(text, max_length=80, min_length=30, do_sample=False)
        st.subheader("Summary")
        st.success(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text.")
