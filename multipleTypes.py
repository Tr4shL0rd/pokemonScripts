from sys import argv

def hexToRGB(hex):
    hex = hex.lstrip("#")
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
def hexToAnsi(hex,typename):
    debug=False
    rgb = hexToRGB(hex)
    ansi = "\033["
    ansi += f"38;2;{rgb[0]};{rgb[1]};{rgb[2]}" 
    ansi += "m"
    ansi += typename
    if debug:
        ansi += "("+hex+")"
    ansi += "\033[0m"
    return ansi

def flatten(arr:list) -> list:
    flat = []
    for elem in arr:
        if type(elem) == list:
            flat += flatten(elem)
        else:
            flat.append(elem)
    return flat

def prettify(arr:list):
    string = ""
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return f"{arr[0]} and {arr[1]}"
    else:
        for elem in arr:
            if elem == arr[-1]:
                string += f"and {arr[-1]}"
                break
            if elem is not arr[-1]:
                string += f"{elem}, "
    if len(arr) != 2:
        return string.replace(", and", " and")
    return string

def typeInteraction():
    colors = {
        "normal":   "#A8A77A",
        "fire":     "#EE8130",
        "water":    "#6390F0",
        "electric": "#F7D02C",
        "grass":    "#7AC74C",
        "ice":      "#96D9D6",
        "fighting": "#C22E28",
        "poison":   "#A33EA1",
        "ground":   "#E2BF65",
        "flying":   "#A98FF3",
        "psychic":  "#F95587",
        "bug":      "#A6B91A",
        "rock":     "#B6A136",
        "ghost":    "#735797",
        "dragon":   "#6F35FC",
        "dark":     "#705746",
        "steel":    "#B7B7CE",
        "fairy":    "#D685AD"
    }
    normal   = hexToAnsi(colors["normal"],"Normal".upper())
    fire     = hexToAnsi(colors["fire"],"Fire".upper())
    water    = hexToAnsi(colors["water"],"Water".upper())
    electric = hexToAnsi(colors["electric"],"Electric".upper())
    grass    = hexToAnsi(colors["grass"],"Grass".upper())
    ice      = hexToAnsi(colors["ice"],"Ice".upper())
    fighting = hexToAnsi(colors["fighting"],"Fighting".upper())
    poison   = hexToAnsi(colors["poison"],"Poison".upper())
    ground   = hexToAnsi(colors["ground"],"Ground".upper())
    flying   = hexToAnsi(colors["flying"],"Flying".upper())
    psychic  = hexToAnsi(colors["psychic"],"Psychic".upper())
    bug      = hexToAnsi(colors["bug"],"Bug".upper())
    rock     = hexToAnsi(colors["rock"],"Rock".upper())
    ghost    = hexToAnsi(colors["ghost"],"Ghost".upper())
    dragon   = hexToAnsi(colors["dragon"],"Dragon".upper())
    dark     = hexToAnsi(colors["dark"],"Dark".upper())
    steel    = hexToAnsi(colors["steel"],"Steel".upper())
    fairy    = hexToAnsi(colors["fairy"],"Fairy".upper())
    types = {
        "Bug":      [fire,     flying, rock],
        "Ice":      [fighting, fire, rock, steel],
        "Fire":     [ground,   rock, water],
        "Dark":     [bug,      fairy, fighting],
        "Rock":     [fighting, grass, ground, steel, water],
        "Ghost":    [dark,     ghost],
        "Steel":    [fighting, fire, ground],
        "Grass":    [bug,      fire, flying, ice, poison],
        "Fairy":    [poison,   steel],
        "Water":    [electric, grass],
        "Normal":   [fighting],
        "Flying":   [electric, ice, rock],
        "Poison":   [ground,   psychic],
        "Ground":   [grass,    ice, water],
        "Psychic":  [bug,      dark, ghost],
        "Dragon":   [dragon,   fairy, ice],
        "Fighting": [fairy,    flying, psychic],
        "Electric": [ground]
    }
    
    while True:
        typing = input("types: ").title().strip().split()
        if len(typing) == 2:
            weaknesses = [types[typing[0]], types[typing[1]]]
            weaknesses = list(set(flatten(weaknesses)))    

        if len(typing) == 1:
            print(f"{hexToAnsi(colors[typing[0].lower()], typing[0].upper())} is weak against: {prettify(types[typing[0]])}")
        else:
            print(f"{hexToAnsi(colors[typing[0].lower()], typing[0].upper())} and {hexToAnsi(colors[typing[1].lower()], typing[1].upper())} is weak against: {prettify(weaknesses)}")
        print()
typeInteraction()
