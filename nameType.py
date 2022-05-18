import sys
import requests
import json
from multipleTypes import hexToRGB, hexToAnsi, prettify, warningAnsi, clear, banner, flatten, underline
linux    = sys.platform == "linux"
windows  = sys.platform == "win32" or sys.platform == "cywig"
macOS    = sys.platform == "darwin"
aix      = sys.platform == "AIX"
if linux:
	import readline

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
	ice      = hexToAnsi(colors["ice"],     "Ice".upper())
	bug      = hexToAnsi(colors["bug"],     "Bug".upper())
	fire     = hexToAnsi(colors["fire"],    "Fire".upper())
	dark     = hexToAnsi(colors["dark"],    "Dark".upper())
	rock     = hexToAnsi(colors["rock"],    "Rock".upper())
	ghost    = hexToAnsi(colors["ghost"],   "Ghost".upper())
	steel    = hexToAnsi(colors["steel"],   "Steel".upper())
	grass    = hexToAnsi(colors["grass"],   "Grass".upper())
	fairy    = hexToAnsi(colors["fairy"],   "Fairy".upper())
	water    = hexToAnsi(colors["water"],   "Water".upper())
	normal   = hexToAnsi(colors["normal"],  "Normal".upper())
	flying   = hexToAnsi(colors["flying"],  "Flying".upper())
	poison   = hexToAnsi(colors["poison"],  "Poison".upper())
	ground   = hexToAnsi(colors["ground"],  "Ground".upper())
	dragon   = hexToAnsi(colors["dragon"],  "Dragon".upper())
	psychic  = hexToAnsi(colors["psychic"], "Psychic".upper())
	fighting = hexToAnsi(colors["fighting"],"Fighting".upper())
	electric = hexToAnsi(colors["electric"],"Electric".upper())
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

	print(f"{name.title()}: {PokeTypes}")
	print(f"National Pokedex ID: {data['id']}")
	print(f"{name.title()} is {underline('WEAK')} to {prettify(weakTypes[pokeTypes[0].title()])}")
	print()
while True:
	commands = {
			"help": " Shows This Message", 
			"clear": "Clears the screen",
			"exit": "Exits the program",
			"banner": "Shows the banner",
		}
	
	EXIT_ALIAS = ["stop", "quit", "exit"]
	HELP_ALIAS = ["help", "?"]
	COMMANDS = list(set(flatten([list(commands.keys()) + EXIT_ALIAS + HELP_ALIAS])))
	if linux:
			readline.parse_and_bind("tab: complete")
			def complete(text,state):
				volcab = flatten([COMMANDS])
				results = [x for x in volcab if x.startswith(text)] + [None]
				return results[state]
			readline.set_completer(complete)
	try:
		name = input("Pokemon Name: ").lower().strip()
		print()
		# Command Handling
		if name in COMMANDS:
			if name in HELP_ALIAS:
				print(f"{'='*50}")
				for k,v in commands.items():
					print(f"{k}: {v}")
				print(f"{'='*50}\n")
			elif name == "clear":
				clear()
			elif name == "banner":
				print(banner("POKEMON  TYPES", 50))
			elif name in EXIT_ALIAS:
				print("Exiting...")
				exit()
			continue
			
		url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
		r = requests.get(url)
		main(name)
	except json.decoder.JSONDecodeError as PokemonNotFound:
		print(warningAnsi(f"\"{name}\" Not Found!\n"))
	except KeyboardInterrupt:
		print("\nExiting...")
		exit()