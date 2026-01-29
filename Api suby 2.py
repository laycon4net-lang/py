import requests
url = "https://api.adviceslip.com/advice"
def get_random_technology_fact():
    response = requests.get(url)
    if response.status_code ==200:
        fact_data = response.json()
        print(f"Did you know? ",response.text)
    else:
        print("Faied to fetch fact")
while True:
            user_input = input("press Enter to get a random technology fact or type 'q' to quit...")
            if user_input.lower() == 'q': 
                break
            get_random_technology_fact()