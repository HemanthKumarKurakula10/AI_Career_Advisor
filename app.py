import os
import json
from datetime import datetime
import streamlit as st
from ctransformers import AutoModelForCausalLM

# --------------------------- Configuration ---------------------------
CORPUS_PATH = "career_corpus/corpus.jsonl"
os.makedirs(os.path.dirname(CORPUS_PATH), exist_ok=True)

# Create empty file if not exists
if not os.path.exists(CORPUS_PATH):
    with open(CORPUS_PATH, "w", encoding="utf-8") as f:
        pass

# Simple password for admin access (change for production)
ADMIN_PASSWORD = "admin123"

# --------------------------- Load CTransformers Model ---------------------------
@st.cache_resource
def load_model():
    model = AutoModelForCausalLM.from_pretrained(
        "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF",
        model_file="tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
        model_type="llama",
        max_new_tokens=256,
        temperature=0.7,
        repetition_penalty=1.1
    )
    return model

llm = load_model()

# --------------------------- Streamlit UI ---------------------------
st.set_page_config(page_title="AI Career Advisor", page_icon="🎓")
st.title("🎓 AI Career Advisor")
st.markdown("Get personalized career guidance powered by AI – in your language!")

st.subheader("🔍 What are your interests or career goals?")
user_input = st.text_area("Tell us what you want to do, learn, or become.")

language = st.selectbox("🌐 Select your language", ["English", "Telugu", "Hindi", "Tamil", "Malayalam", "Kannada", "other"])

if st.button("🧠 Get Career Advice"):
    if user_input.strip() == "":
        st.warning("Please enter something.")
    else:
        prompt = f"### Instruction:\nGive personalized career advice to someone who said: '{user_input}'\n\n### Response:"
        output = llm(prompt)

        # Get first 3 sentences for readability
        advice = '. '.join(output.split('. ')[:3]) + '.'

        st.markdown("### 🎯 Career Guidance")
        st.success(advice)

        # Save user input and advice to corpus
        entry = {
            "timestamp": str(datetime.now()),
            "user_input": user_input,
            "language": language,
            "ai_advice": advice
        }

        with open(CORPUS_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")

# --------------------------- Admin Corpus Viewer ---------------------------
with st.expander("📚 View AI Learning Corpus (Admin Only)"):
    admin_access = st.text_input("Enter admin password to view stored data:", type="password")

    if admin_access == ADMIN_PASSWORD:
        show_corpus = st.checkbox("✅ Show stored user queries")

        if show_corpus:
            st.markdown("---")
            st.subheader("🧠 Stored AI Learning Corpus")
            try:
                with open(CORPUS_PATH, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    if not lines:
                        st.info("No entries in the corpus yet.")
                    for i, line in enumerate(lines, 1):
                        entry = json.loads(line)
                        st.markdown(f"**{i}.** ({entry['timestamp']})")
                        st.write(f"**Language:** {entry['language']}")
                        st.write(f"**User Query:** {entry['user_input']}")
                        st.write(f"**AI Advice:** \"{entry['ai_advice']}\"")
                        st.markdown("---")
            except Exception as e:
                st.error(f"Failed to read corpus: {e}")

        # ✅ Add Download Button for JSONL File
        with open(CORPUS_PATH, "rb") as f:
            st.download_button(
                label="⬇️ Download Full Corpus (.jsonl)",
                data=f,
                file_name="ai_learning_corpus.jsonl",
                mime="application/json"
            )
    elif admin_access != "":
        st.error("❌ Incorrect password. Access denied.")
