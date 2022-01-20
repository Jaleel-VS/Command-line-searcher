from sys import argv, exit
from os import system


user_input = argv
if len(user_input) < 2:
    print("Please input a search term")
    exit()

search_term = '+'.join(user_input[1:])
google_query = f"https://www.google.com/search?q={search_term}"

system(f"xdg-open {google_query} &> /dev/null")
