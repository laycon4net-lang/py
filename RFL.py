import cohere, config, time
co = cohere.Client(config.COHERE_API_KEY)
def ai(prompt, temp=0.3):
    try:
        return co.chat(
            model="command-r-08-2024",
            message=prompt,
            temperature=temp,
            max_tokens=200
        ).text.strip()
    except Exception as e:
      return f"Error : {e}"
def feedback():
    p = input ("prompt:  ")
    r = ai(p)
    print("\nAI:", r)
    print("\nImproved:\n", r + "\na[Feedback: "+ input("youre feedback:") + "]")
def role():
    c = input("Category: ")
    t = input("Topic: ")
    print("\nTeacher:\n", ai(f"Explain {t} simply."))
    time.sleep(1)
    print("\nExpert:\n", ai(f"As an expert in {c}, explain {t} in detail."))
def temp_test():
    p = input("creative prompt:")
    for t in (0.1, 0.5, 0.9):
        print(f"\ntemp {t}:\n", ai(p, t))
        time.sleep(1)
def main():
    funcs = {"1": feedback 2.Role 3.Temp }
