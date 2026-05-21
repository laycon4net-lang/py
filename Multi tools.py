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
          cont = generate (
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
     temp = st.slider("Creativity level", 0.0, 1.0, 0.3)
     tokens = st.slider("Max Tokens (Response Length)", 200, 2000, 1000)
     col1, col2 = st.colums([1,2])
     if col1.button(" Clear"):
          st.session_state.history_ata:
          col2.download_button(
               "Export",
               export_txt(st.session_state.history_ata),
               "Teaching_Assistant_chat.txt",
               "text/plain"
          )
          q = st.text_input("Enter your question:")
          if st.button("Ask"):
               if not q.strip():
                    st.warming("Enter a question.")
                else:
                    with st.spinner("Thinking..."):
                        prompt = q
                        if st.session_state.history_ata:
                            previous = "\n".join(
                                 [f"Q: {h['question']}\nA: {h['answer']}"
                            )
                            for h in st.session_state.history_ata[:3]]
                            )
                            prompt = previous + "\nCurrent Question: " + q
                            ans = generate_Complete(prompt, temp, tokens)
                           if not st.session_state.History_ata:
                              return.markdown(" Conversation History")
                            for i, h in enumerate(st.session_state.history_ata, 1):
                                st.markdown(f**Q[i]: {h['question']}**")
                                st.markdown(h["answer"])
                                st.markdown("")

                                

          
    
         