from sys import argv
def prettify(arr:list):
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
    if len(arr) != 2:
        return string.replace(", and", " and")
    return string
def typeInteraction(type):
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
    if len(argv) != 2:
        type = input("pokemon type: ").strip()
    if type not in types:
        print(f"\"{type}\" is not a valid type!")
        exit()
    Typing = [Typing for Typing in types[type]]
    print(f"{type} is weak against: {prettify(Typing)}")
typeInteraction(argv[1].lower().title())