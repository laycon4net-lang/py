import cohere
import config
co = cohere.Client(config.COHERE_API_KEY)
def generate_resonse(prompt):
    try:
        response = co.chat(
            model="c4ai-aya-expanse-8b",
            message=prompt,

            max_tokens=200
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"
def prompt_engineering_project():
    print("=" * 60)
    print("REAL PROMPT ENGINERRING PROJECT (COHERE API)")
    print("Ask ANY question - get REAL AI response")
    print("=" * 60)
    
    user_prompt = input("\eENTER your question: ")
    print("\n AI Response:")
    print(generate_resonse(user_prompt))
if __name__ == "__main__":
    prompt_engineering_project()
