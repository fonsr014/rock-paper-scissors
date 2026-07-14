import random
import time

# mg this is not json, although i guess the syntax is the same BUT IT IS STILL VALID PYTHON!
# also tbh i used google just to see what beats what in this version of the game, nothing else
definitions = [
    {
        "name": "Rock",
        "beats": ["Scissors", "Sponge", "Fire"]
    },
    {
        "name": "Paper",
        "beats": ["Rock", "Air", "Water"]
    },
    {
        "name": "Scissors",
        "beats": ["Paper", "Air", "Sponge"]
    },
    {
        "name": "Fire",
        "beats": ["Scissors", "Paper", "Sponge"]
    },
    {
        "name": "Sponge",
        "beats": ["Water", "Paper", "Air"]
    },
    {
        "name": "Air",
        "beats": ["Fire", "Water", "Rock"]
    },
    {
        "name": "Water",
        "beats": ["Fire", "Rock", "Scissors"]
    }
]

def choose_amount():
    try:
        amount = int(input("How many items do you want?\n\x1b[2mYou may enter between 3 and 7 items.\x1b[0m\n"))
        if amount >= 3 and amount <= 7:
            return amount
        else:
            return None
    except:
        return None
    
def pick_option(many: int):
    try:
        built_string = ""
        for i in range(many):
            built_string += f"{i+1}. {definitions[i]["name"]}\n" # i made this so that the list changes depending on how many items the player chose
        amount = int(input(f"Choose your option:\n\x1b[2m{built_string}\x1b[0m\n"))
        if amount > 0 and amount <= many:
            return amount
        else:
            return None
    except:
        return None

def main():
    amount = None
    while amount == None:
        amount = choose_amount()
    
    robot_pick = random.randint(0, amount - 1)

    your_pick = None
    while your_pick == None:
        your_pick = pick_option(amount)
    
    print()
    
    time.sleep(0.2)
    for i in range(amount):
        print(f"{definitions[i]["name"]}!")
        time.sleep(0.25)
    
    print()

    print(f"You chose {definitions[your_pick - 1]["name"]}.")
    print(f"AI chose {definitions[robot_pick]["name"]}.")

    winner = None

    for i in definitions[your_pick - 1]["beats"]:
        if i == definitions[robot_pick]["name"]:
            winner = "You win!"
    
    for i in definitions[robot_pick - 1]["beats"]:
        if i == definitions[your_pick]["name"]:
            winner = "AI wins!"
    
    if winner == None:
        winner = "It was a draw..."

    print(f"\n{winner}")

    replay = input("Play again? (Y/N) ")
    if replay.lower() == "y":
        main()

if __name__ == "__main__":
    main()
