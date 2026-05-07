import io 
import streamlit as st
import cohere
import config
co = cohere.Client(config.COHERE_API_KEY)
def generate(prompt):
    try:
        response =co.chat(
            model="command-r-08-2024",
            message=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"
def export_txt(history):
    text = ""
    for i, h in enumerate(history, 1):
        text += f"Q{i}: {h['q']}\nA{i}: {h['a']}\n\n"
    return io.BytesIO(text.encode())
st.title("Math Mastermind")
if "history" not in st.session_state:
    st.session_state.history = []
problem = st.text_area("Enter Math problem")

if st.button("solve"):
    if problem:
        with st.spinner("solving..."):
            answer = generate(problem)
            st.sessions_state.history.insert(
                0, {"q": problem, "a": answer}
            )
if st.session_state.history:
        st.download_button(
            "Export",
            export_txt(st.session_state.history),
            "solutions.txt",
            "text/plain"
        )
        st.subheader("History")
        for item in st.session_state.history:
            st.write("**Q:**", item["q"])
            st.write(item["a"])
            st.write("---")