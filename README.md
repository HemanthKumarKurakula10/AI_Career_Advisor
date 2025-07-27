# 🌐 AI Career Advisor – Multilingual Corpus Builder 🇮🇳🤖

An open-source AI-powered Streamlit app that gives users *career guidance in Indian languages*, while collecting culturally-rich, multilingual data to help build better AI for Bharat.

> Built with ❤ for *Swecha Summer of AI 2025 – Project 2*

---

## 🧠 Problem We Solved

Most existing career guidance platforms:
- Only support English,
- Consume high bandwidth,
- Don’t understand local cultures or contexts.

This project solves that by:
- Giving career suggestions in *regional languages* (like Telugu, Hindi, Tamil, etc.),
- Running even on *low-end systems* and *offline*, and
- Collecting real-world *multilingual career Q&A data* to help AI researchers and developers build inclusive tools.

---

## 🚀 Key Features

✅ Career advice in multiple Indian languages  
✅ Built using open-source *TinyLlama-1.1B-Chat-v1.0-GGUF* model  
✅ Efficient backend using ctransformers (runs locally/offline!)  
✅ Clean UI built with *Streamlit* (mobile-friendly)  
✅ Stores anonymized user queries & AI answers to *build a corpus*  
✅ jsonl download file for *admin users only*  
✅ Deployed on *Hugging Face Spaces*

---

## 🎯 Use Cases

- Rural or non-English speaking students asking about career options  
- Parents seeking guidance in native languages  
- NGOs & EdTechs collecting real-world multilingual training data  
- Researchers building *Indic language models*  

---

## ⚙ Tech Stack

| Component         | Tech Used                                                       |
|------------------|------------------------------------------------------------------|
| Frontend         | Streamlit                                                       |
| Backend Model    | TinyLlama-1.1B-Chat-v1.0-GGUF via ctransformers              |
| Model Provider   | [TheBloke on Hugging Face](https://huggingface.co/TheBloke)     |
| Hosting          | Hugging Face Spaces                                              |
| Language Support | Any language accepted by the model (based on prompt)            |
| Corpus Storage   | jsonl file download                                    |

---
