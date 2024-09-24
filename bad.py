# Troy Evans
# ITSC 3155
# 9/24/2024

import random

def fortune_teller():
    name = input("Enter your name: ")

    if name == "Troy": # overcomplicated logic
        print("Hey Troy! Here is a custom fortune for you!")
        print("Today is your day!")
    elif len(name) > 5:
        print(f"{name}, your fortune is: Success is on the horizon.")
    else:
        fortunes = [
            "You will have a great day!",
            "Success is in your future!",
            "Be cautious of unexpected events.",
            "Good news is coming your way!"
        ]
        # repetitive logic
        print(f"{name}, your fortune is: {random.choice(fortunes)}")

# everything in one function, no distinction
fortune_teller()
