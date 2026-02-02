import cohere
from config import COHERE_API_KEY
co = cohere.Cilent(COHERE_API_KEY)
TOPICS = ["sports", "Technology", "Business", "politics", "Health", ]
def ask_cohere(headline: str):
    prompt = f"""
Classify this news headline into ONE category only. 
categories:
{','.join(TOPICS)}
Headline: "{headline}"
Return ONLY the category name. 
"""
 response = co.chat(
    model="c4ai-aya-expanse-8b",
    message=prompt,
    temprature=0
 )
 return response.text.strip()
def bar():
    return "████████░░"
def show(headline, topic):
    print("\n" + "=" * 60)
    print("News Topic Classifier (cohere API)")
    print("=" * 60)
    print("HEadline:", headline)
    print("Best Topic:", headline)
    print("Best Topic:", topic)
    print("Confidence: ~90% ["+ bar () + "]")
    print("=" * 60)
    def main():
       print("Welcome! Type a news headline and i'll guess the topic.")
       print("Topics:","")