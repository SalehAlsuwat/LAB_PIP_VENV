from colorama import Fore, Back, Style
from art import text2art

print(Fore.CYAN + text2art("Hello Python", font = "banner"))
print(Fore.YELLOW + "=" * 60)
print(Fore.LIGHTGREEN_EX + text2art("SALEH", font = "random"))