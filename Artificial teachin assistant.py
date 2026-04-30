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
    