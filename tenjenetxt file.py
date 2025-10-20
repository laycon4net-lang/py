from colorama import Fore, style, init
from textblob import TextBlob
init(autorest=True)
print(f"{Fore.CYAN}elcome to Sentiment Spy!") {Style.RESET_ALL"}
name = input(f"{Fore.MAGENTA}Enter your name: [Style>RESET_ALL]").strip() or  
            "Agent"
print(f"{Fore.CYAN}Hello Agent {name}! Type 'exit','reset', or 'history'.{style.RESET_All}") 