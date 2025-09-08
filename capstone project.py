import random
def get_difficulty():
    print("/nselect a difficulty level:")
    print("1 - Easy (10 attempts)")
    print("2 - Medium (7 attempts)")
    print("3 - Hard (5 attempts)")
    while True:
     choice = input("Enter your choice (1/2/3):").strip()
     if choice == '1':
        return 10
     elif choice == '2':
        return 7
     elif choice == '3':
        return 5
     else:
          print("Invalid choicce. please enter 1, 2, or 3.")
def play_game():
    name = input("Hello! whats your name?")
    print(f"/nWelcome, {name}! lets play guess the Number")