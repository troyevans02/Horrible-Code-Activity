# Troy Evans
# ITSC 3155
# 9/24/2024

import random

# function to obtain the user's name
def get_user_name():
    return input("Enter your name: ")

# function to generate a fortune
def generate_fortune():
    fortunes = [
        "You'll' have a great day!",
        "Success lies in your future!",
        "Be careful of unexpected events.",
        "Good things are coming your way!"
    ]
    return random.choice(fortunes)

#function to display a fortune
def display_fortune(name, fortune):
    print(f"{name}, your fortune is: {fortune}")

def main():
    name = get_user_name()
    fortune = generate_fortune()
    display_fortune(name, fortune)

if __name__ == "__main__":
    main()
