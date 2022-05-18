import requests
import json
from multipleTypes import hexToRGB, hexToAnsi, prettify

def main(name:str):
    colors = {
            "bug":      "#A6B91A",
            "ice":      "#96D9D6",
            "fire":     "#EE8130",
            "dark":     "#705746",
            "rock":     "#B6A136",
            "ghost":    "#735797",
            "steel":    "#B7B7CE",
            "grass":    "#7AC74C",
            "fairy":    "#D685AD",
            "water":    "#6390F0",
            "normal":   "#A8A77A",
            "flying":   "#A98FF3",
            "poison":   "#A33EA1",
            "ground":   "#E2BF65",
            "dragon":   "#6F35FC",
            "psychic":  "#F95587",
            "fighting": "#C22E28",
            "electric": "#F7D02C",
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
    
    _prettyData = json.dumps(r.json(), indent=4)
    data = r.json()
    pokeTypes = []
    for i in range(len(data["types"])):
        pokeTypes.append(data["types"][i]["type"]["name"])
    if len(pokeTypes) == 1:
        PokeTypes = hexToAnsi(colors[pokeTypes[0].lower()], pokeTypes[0].upper())
    elif len(pokeTypes) == 2:
        PokeTypes = f"{hexToAnsi(colors[pokeTypes[0].lower()], pokeTypes[0].upper())}/{hexToAnsi(colors[pokeTypes[1].lower()], pokeTypes[1].upper())}"

    print(f"{name.title()}: {PokeTypes}\nNational Pokex ID: {data['id']}\n")
    print(f"{name.title()} is weak to {prettify(weakTypes[pokeTypes[0].title()])}")
while True:
    try:
        name = input("Pokemon Name: ")
        url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
        r = requests.get(url)
        main(name)
    except json.decoder.JSONDecodeError:
        print("Invalid Pokemon Name")