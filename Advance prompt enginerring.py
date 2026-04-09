import time
import cohere
import config

co = cohere.Client(config.COHERE_API_KEY)


def generate(prompt, temp=0.5):
    try:
        res = co.chat(
            model="c4ai-aya-expanse-8b",
            message=prompt,
            temperature=temp,
            max_tokens=200
        )
        return res.text.strip()
    except Exception as e:
        return f"Error: {e}"


def main():
    print("\n=== TEMPERATURE DEMO ===")

    prompt = input("Enter a creative prompt: ")

    for t in [0.1, 0.5, 0.9]:
        print(f"\nTemp {t}:")
        print(generate(prompt, t))
        time.sleep(1)

    print("\n=== INSTRUCTION DEMO ===")

    topic = input("Enter a topic: ")
    tasks = [
        f"Summarize {topic}",
        f"Explain {topic} to a child",
        f"Pros and cons of {topic}",
        f"Future headline about {topic}"
    ]

    for task in tasks:
        print(f"\n{task}:")
        print(generate(task, 0.7))
        time.sleep(1)


if __name__ == "__main__":
    main()