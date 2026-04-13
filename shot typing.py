import cohere
from config import COHERE_API_KEY

if not COHERE_API_KEY:
    print("❌ API key missing")
    exit()

co = cohere.Client(COHERE_API_KEY)

def gen(prompt, temp=0.5):
    return co.chat(
        model="command-r-08-2024",
        message=prompt,
        temperature=temp,
        max_tokens=200
    ).text.strip()

def run():
    print("\nZERO / ONE / FEW-SHOT ACTIVITY\n")

    cat = input("Category: ").strip()
    item = input("Item: ").strip()

    if not cat or not item:
        print("❌ Missing input")
        return

    print("\n--- ZERO-SHOT ---")
    print(gen(f"Is {item} a {cat}? Yes or No.", 0.3))

    print("\n--- ONE-SHOT ---")
    print(gen(f"fruit: apple → Yes\n{cat}: {item} →", 0.3))

    print("\n--- FEW-SHOT ---")
    print(gen(f"fruit: apple → Yes\nanimal: dog → Yes\n{cat}: {item} →", 0.3))

    print("\n--- CREATIVE ---")
    print(gen(f"One-line story about '{item}':", 0.7))

if __name__ == "__main__":
    run()