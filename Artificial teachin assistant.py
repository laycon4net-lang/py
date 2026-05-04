import io
import streamlit as st
import cohere
import config
co = cohere.Client(config.COHERE_API_KEY)
def generate_response(prompt):
    try:
        res = co.chat(
            model="command-r-08-2024",
            message=prompt,
            temperature=0.3,
            max_tokens=300
        )
        return res.text.strip()
    except Exception as e:
        return f"Error: {e}"
CSS = """
<style>
.history-wrap {max-height: 420px; overflow-y: auto; padding-right: 6px;}
.qa-card{
    border: 1px solid #e6e6e6;
    background: #ffffff;
    border-radius: 10px 0;
    padding: 14px 16px;
    margin: 10px 0;
    box-shadow: 0 1px 2px rgba(0,0,0,0.04);
}
.q{font-weight: 700; color: #0a6ebd; margin-bottom: 8px;}
.a{white-space: pre-wrap; color: #333; line-height: 1.5;}
</style>
"""
def export_bytes(history):
    text = "\n\n".join(
        [f"Q{1}: {h['question']}\nA{i}: {h['answer']}" for i, h in enumerate(history, 1)]
    )
    return io.BytesIO(text.encode("utf-8"))
def main():
    st.set_page_config("AI Teaching Assistant", layout="centered")
    st.title("AI Teaching Assistant (Cohere)")
    history = st.session_state.setdefault("history", [])
    coll, col2 = st.columns([1, 2])
    if coll.button(" Clear"):
        history.clear()
        st.rerun()
    if history:
            col2.download_button("Export", export_bytes(history), "chat.txt")
    q = st.text_input("Ask a question:")
    if st.button("Ask"):
                if q.strip():
                    with st.spinner("Thinking..."):
                        a = generate_response(q)
                    history.insert(0, {"question": q, "answer": a})
                    st.rerun()
                else:
                     st.warning("Enter a question.")
    st.subheader("History")
    for i, h in enumerate(history, 1):
        st.markdown(f"**Q{i}:** {h['question']}")
        st.markdown(f"{h['answer']}")

        st.divider()

if __name__ == "__main__":

   main()
   
    