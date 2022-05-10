import random
import time
from sys import argv
if len(argv) == 2:
    if argv[1] == "reset":
        with open("usedNames.txt", "w") as f:
            f.write("")
        exit()
timeout = time.time() + 0.1

def flatten(arr:list) -> list:
    flat = []
    for elem in arr:
        if type(elem) == list:
            flat += flatten(elem)
        else:
            flat.append(elem)
    return flat


with open("usedNames.txt", "r") as f:
    usedNames = f.read().splitlines()

categories = {
        "foodNames":  ["pasta", "noodle", "rice", "cinnamon bun", "peanut", "spaghetti", "pizza", "burger"],
        "humanNames": ["alan", "bob", "john", "mark", "james", "jaiden", "david"], 
        "weirdNames": ["phuck boi", "thanks obama", "mole man", "thumper", "dumbo", "whiskers", "memes", "dumb_dumb", "whoops", "failure", "wrong", "daddy", "mommy"]
    }

def rng():
    categoryRNG = random.choice(list(categories.keys()))
    return f"{categoryRNG}: {random.choice(categories[categoryRNG]).title()}"
RNG = rng()
while RNG in usedNames:
    RNG = rng()
    if time.time() > timeout:
        print("No more names available")
        exit()

print(RNG)

with open("usedNames.txt", "a") as f:
    f.write(f"{RNG}\n")
with open("usedNames.txt", "r") as f:
    usedNames = f.read().splitlines()

