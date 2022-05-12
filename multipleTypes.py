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
        ansi += f"[{hex}]"
    ansi += "\033[0m"
    return ansi

def warningAnsi(message):
    return "\033[4;31;31m" + message + "\033[0m"

def flatten(arr:list) -> list:
    flat = []
    for elem in arr:
        if type(elem) == list:
            flat += flatten(elem)
        else:
            flat.append(elem)
    return flat

def prettify(arr:list):
    if len(arr) == 0:
        return "NOTHING"
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
    if len(arr) >= 2:
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
    bug      = hexToAnsi(colors["bug"],"Bug".upper())
    ice      = hexToAnsi(colors["ice"],"Ice".upper())
    fire     = hexToAnsi(colors["fire"],"Fire".upper())
    dark     = hexToAnsi(colors["dark"],"Dark".upper())
    rock     = hexToAnsi(colors["rock"],"Rock".upper())
    ghost    = hexToAnsi(colors["ghost"],"Ghost".upper())
    steel    = hexToAnsi(colors["steel"],"Steel".upper())
    grass    = hexToAnsi(colors["grass"],"Grass".upper())
    fairy    = hexToAnsi(colors["fairy"],"Fairy".upper())
    water    = hexToAnsi(colors["water"],"Water".upper())
    normal   = hexToAnsi(colors["normal"],"Normal".upper())
    flying   = hexToAnsi(colors["flying"],"Flying".upper())
    poison   = hexToAnsi(colors["poison"],"Poison".upper())
    ground   = hexToAnsi(colors["ground"],"Ground".upper())
    dragon   = hexToAnsi(colors["dragon"],"Dragon".upper())
    psychic  = hexToAnsi(colors["psychic"],"Psychic".upper())
    fighting = hexToAnsi(colors["fighting"],"Fighting".upper())
    electric = hexToAnsi(colors["electric"],"Electric".upper())
    TYPES = [bug, ice, fire, dark, rock, ghost, steel, grass, fairy, water, normal, flying, poison, ground, dragon, psychic, fighting, electric]
    CLEAR_TYPES = ["Bug", "Ice", "Fire", "Dark", "Rock", "Ghost", "Steel", "Grass", "Fairy", "Water", "Normal", "Flying", "Poison", "Ground", "Dragon", "Psychic", "Fighting", "Electric"]
    # "TYPE": "[WEAKNESS]"
    weakTypes = {
        "Bug":      [fire, flying, rock],
        "Ice":      [fighting, fire, rock, steel],
        "Fire":     [ground, rock, water],
        "Dark":     [bug, fairy, fighting],
        "Rock":     [fighting, grass, ground, steel, water],
        "Ghost":    [dark, ghost],
        "Steel":    [fighting, fire, ground],
        "Grass":    [bug, fire, flying, ice, poison],
        "Fairy":    [poison, steel],
        "Water":    [electric, grass],
        "Normal":   [fighting],
        "Flying":   [electric, ice, rock],
        "Poison":   [ground, psychic],
        "Ground":   [grass, ice, water],
        "Dragon":   [dragon, fairy, ice],
        "Psychic":  [bug, dark, ghost],
        "Fighting": [fairy, flying, psychic],
        "Electric": [ground]
    }
    strongTypes = {
        "Bug":      [grass, dark, psychic],
        "Ice":      [dragon, flying, grass, ground],
        "Fire":     [bug, grass, ice, steel],
        "Dark":     [ghost, psychic],
        "Rock":     [bug, fire, flying, ice],
        "Ghost":    [ghost, psychic],
        "Steel":    [fairy, ice, rock],
        "Grass":    [ground, rock, water],
        "Fairy":    [fighting, dark, dragon],
        "Water":    [fire, ground, rock],
        "Normal":   [],
        "Flying":   [bug, fighting, grass],
        "Poison":   [fairy, grass],
        "Ground":   [electric, fire, poison, rock, steel],
        "Dragon":   [dragon],
        "Psychic":  [fighting, poison],
        "Fighting": [dark, ice, normal, rock, steel],
        "Electric": [flying, water]
    }
    
    while True:
        try:
            typing = input("type(s): ").title().strip().split()
        except KeyboardInterrupt:
            print("\nexiting...")
            exit()
        if typing[0] not in CLEAR_TYPES or typing[1] not in CLEAR_TYPES:
            print(warningAnsi(f"\n{str(typing)} ARE INVALID TYPE(S)!\n"))
            typeInteraction()
        if len(typing) >= 3:
            print("Max 2 types")
            typeInteraction()
        if typing[0].lower() == "types":
            print("\n".join(flatten(list(TYPES))))
            typeInteraction()
        if len(typing) == 2:
            weaknesses = [weakTypes[typing[0]], weakTypes[typing[1]]]
            weaknesses = list(set(flatten(weaknesses)))    
            strengths = [strongTypes[typing[0]], strongTypes[typing[1]]]
            strengths = list(set(flatten(strengths)))

        if len(typing) == 1:
            print(f"{hexToAnsi(colors[typing[0].lower()], typing[0].upper())} is WEAK against: {prettify(weakTypes[typing[0]])}")
            print(f"{hexToAnsi(colors[typing[0].lower()], typing[0].upper())} is SUPER EFFECTIVE against: {prettify(strongTypes[typing[0]])}")
        elif len(typing) >= 2:
            print(f"{hexToAnsi(colors[typing[0].lower()], typing[0].upper())} and {hexToAnsi(colors[typing[1].lower()], typing[1].upper())} is WEAK against: {prettify(weaknesses)}")
            print(f"{hexToAnsi(colors[typing[0].lower()], typing[0].upper())} and {hexToAnsi(colors[typing[1].lower()], typing[1].upper())} is SUPER EFFECTIVE against: {prettify(strengths)}")
        print()
typeInteraction()
