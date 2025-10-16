print("hello! I am AI Bot. What's your name? : ")
name = input()
print(f"Nice to meet you, {name} ! ")
print("how are you felling today? (good/bad) : ")
mood = input().lower()
if mood == "good":
 print("I'm glad to her that!")
elif mood == "bad":
 print("I'm sorry to hear that. Hope things get better soon.")
else:
   print("I see. sometimes it's hard to put feelings into words.")
print(f"It was nice chatting with you {name}. Goodbye!")