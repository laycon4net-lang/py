import cohere
import config
co = cohere.Client(config.COHERE_API_KEY)
def generate_response(prompt, temprature=0.3):
    try:
        response = co.chat(
            model="command-r-08-2024",
            message=prompt,
            temprature=temprature,
            max_tokens=800
        )
        return response.text.strrip()
    except Exception as e:
        return f"Error: {e}"
def get_essay_details():
        print("\n=== AI Writing Assistant ===\n")
        topic = input("Topics: ").strip()
        essay_type = input("Essay type: ").strip()
        length = input("Target audience: ").strip()
        audience = input("Target audience: ").strip()
        return topic, essay_type, length, audience
def generate_essay(topic, essay_type, length, audience):
     try:
           temp - float(input("Temprature (0.1-0.7): ").strip())
     except:
          temp = 0.3
          sections ={
               "Introduction": f"Write an introduction for a {essay_type} essay about{topic} in {length}. Audience: {audience}.",
               "Body": f"Write the body of a {essay_type} essay about {topic} for {audience}.",
               "Conclusion": f"Write a strong conclusion for a {essay_type} essay about {topic} for {audience}."
               
          }
          for title, prompt in sections.items():
               print(f)
        
        
    
        