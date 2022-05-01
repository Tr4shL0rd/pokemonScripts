###
# FORMAT: userType: targetType
# FORMAT: fire is weak to water
###
import sys

def prettifyArrOutput(arr):
    string = ""
    if len(arr) == 1:
        return arr[0].title()
    elif len(arr) == 2:
        return f"{arr[0].title()} and {arr[1].title()}"
    else:
        for elem in arr:
            if elem == arr[-1]:
                string += f"and {arr[-1].title()}"
                break
            if elem is not arr[-1]:
                string += f"{elem.title()}, "
    return string

def main(type):
    type = type.title()
    types = {
        "Bug": ["Fire", "Flying", "Rock"],
        "Ice": ["Fighting","Fire", "Rock", "Steel"],
        "Fire": ["Ground","Rock", "Water"],
        "Dark": ["Bug", "Fairy", "Fighting"],
        "Rock": ["Fighting", "Grass", "Ground", "Steel", "Water"],
        "Ghost": ["Dark", "Ghost"],
        "Steel": ["Fighting", "Fire", "Ground"],
        "Grass": ["Bug","Fire", "Flying", "Ice", "Poison"],
        "Fairy": ["Poison", "Steel"],
        "Water": ["Electric", "Grass"],
        "Normal": ["Fighting"],
        "Flying": ["Electric", "Ice", "Rock"],
        "Poison": ["Ground", "Psychic"],
        "Ground": ["Grass", "Ice", "Water"],
        "Psychic": ["Bug", "Dark", "Ghost"],
        "Dragon": ["Dragon", "Fairy", "Ice"],
        "Fighting": ["Fairy", "Flying", "Psychic"],
        "Electric": ["Ground"]
    }

    data = prettifyArrOutput(list(types[type]))
    lastComma = revData = data[::-1]
    X = len(data) - lastComma.index(",")-1
    print(f"{type} is weak against {data[:X]+data[X+1:]}")
types = ["Bug", "Ice", "Fire", "Dark", "Rock", "Ghost", "Steel", "Grass", "Fairy", "Water", "Normal", "Flying", "Poison", "Ground", "Psychic", "Dragon", "Fighting", "Electric",]
if len(sys.argv) == 2:
    type = sys.argv[1].strip()
else:
    type = input("pokemon type: ")
if type not in types:
    print(f"\"{type}\" is not a valid type!")
    exit()
main(type)
