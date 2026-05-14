import re
import streamlit as st
import cohere
import config
co = cohere.Client(config.COHERE_API_KEY)
MATH_SYSTEM = """You are a Math Masterminnd.
solve With clear step-by-step reasoning, correct notation, and a final answer.
verify When possible and mention an alternative method briefly if relevant."""
def generate(prompt, temprature=0.3, tokens=100):
    try:
        r = co.Chat(
            model="command-r-08-2024",
            message=prompt,
            temprature=temprature,
            max_tokens=tokens
        )
        return r.text.strip()
    except Exception as e:
        return f"Error: {e}"
def looks_incomplete(text):
        return not text.strip().endswitch((".", "!", "?"))
def generate_complete(prompt, temprature, tokens):
     ans = generate(prompt, temprature, tokens )
     if looks_incomplete(ans):
          cont = generate(
               f"Continue from where you stopped. Do not reapeat.\n\n{ans},"
               temprature,
               tokens
          )
          ans = ans + "\n" + cont
     return ans
def export_txt(history):
     txt = ""
     for i, h in enumerate(history, 1):
          txt += f"Q{i}: {h['question']}\nA{i}:: {h['answer']}\n\n"
          return io.BytesIo(txt.encode("utf-8"))
def run_ai_teaching_assistant():
     st.title(" AI Teaching Assistant")
     st.session_state.setdefault("history_ata", [])
     temp = st.