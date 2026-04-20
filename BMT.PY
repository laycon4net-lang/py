import cohere, config
co = cohere.Client(config.COHERE_API_KEY)
def generate(prompt, temp=0.3, token=400):
    try:
        res = co.chat(
            model="command-r-08-2024",
            message=prompt,
            temperature=temp,
            max_tokens=token

        )
        return res.text.strip()
    except Exception as e:
        return f"Error: {e}"
def bias_activity():
    print("\n=== BIAS MITIGATION ===")
    p = input("Enter prompt: ").strip()
    if not p: return print("Empty prompt.")
    print("\nInitial:\n", generate(p))
    n = input("\nNeutral prompt: ").strip()
    if n:
        print("\nNeutral Response:\n", generate(n))
    else:
        print("Skipped.")
def token_activity():
    print("\n=== TOKEN TEST ===")
    lp = input("Long prompt: ").strip()
    if lp:
        res = generate(lp, token=800)
        print("\nPreview:\n", res[:500] + ("..." if len(res) > 500 else""))
        sp = input("\nShort prompt: ").strip()
        if sp:
            print("\nResponse:\n", generate(sp, tokens=250))
def main():
    while True:
        print("\n1. Bias 2. Token 3. EXit")
        c = input("choice: ").strip()
        if c == "1": bias_activity()
        elif c == "2": token_activity()
        elif c == "3": break

        else: print("Invalid choice.")

if __name__ == "__main__":

    main()

