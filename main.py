import random
import json
import time

definitions = ["Rock", "Paper", "Scissors", "Fire", "Sponge", "Air", "Water"]
fight = [
    [0, ]
    []
    []
    []
]

def choose():
    try:
        amount = int(input("How many items do you want?\n\x1b[2mYou may enter between 3 and 7 items.\x1b[0m\n"))
        if amount >= 3 and amount <= 7:
            return amount
        else:
            return None
    except:
        return None

def main():
    amount = None
    while amount == None:
        amount = choose()

if __name__ == "__main__":
    main()
