import os 
if os.name == "posix":
	import readline

from pyfiglet import Figlet


def banner():
	pad = "="*80
	return f'{pad}\n{Figlet(font="slant").renderText("POKEMON  TYPE  CHART")}Created By Tr4shL0rd\n{pad}\n'
print(banner())
def moveCursor(x,y):
	print("\n"*100)
	print(f"\033[{y};{x}H", end="")

def hexToRGB(hex):
	hex = hex.lstrip("#")
	return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def removeColor(string):
	string = string.replace("\033[", "").replace("m", "").replace(";", ",")
	string = "".join([i for i in string if not i.isdigit()])
	return string.replace(",", "").title()

def hexToAnsi(hex,typename):
	debug=False
	rgb  = hexToRGB(hex)
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
	CLEAR_TYPES = [removeColor(PLAIN_TYPES) for PLAIN_TYPES in TYPES]
	#CLEAR_TYPES = ["Bug", "Ice", "Fire", "Dark", "Rock", "Ghost", "Steel", "Grass", "Fairy", "Water", "Normal", "Flying", "Poison", "Ground", "Dragon", "Psychic", "Fighting", "Electric"]
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
		commands = {
			"help": " Shows This Message", 
			"types": "Shows the whole list of pokemon types",
			"clear": "Clears the screen",
			"exit": "Exits the program",
			"banner": "Shows the banner",
		}
		COMMANDS = list(commands.keys())
		# Auto completion for commands
		if os.name == "posix":
			readline.parse_and_bind("tab: complete")
			def complete(text,state):
				volcab = flatten([COMMANDS])
				results = [x for x in volcab if x.startswith(text)] + [None]
				return results[state]
			readline.set_completer(complete)

		try:
			typing = input("Type(s): ").title().strip().split()
		except KeyboardInterrupt:
			print("\nexiting...")
			exit()
		# COMMAND CHECK
		commandInput = typing[0].lower()
		if commandInput in COMMANDS:
			if commandInput == "help":
				print(f"\n{'='*50}")
				for k,v in commands.items():
					print(f"{k}: {v}")
				print(f"{'='*50}\n")
				continue
			elif commandInput == "types":
				print("\n".join(flatten(list(TYPES))))
				continue
			elif commandInput == "clear":
				moveCursor(1,1)
				continue
			elif commandInput == "exit":
				print("exiting...")
				exit()
			elif commandInput == "banner":
				print(banner())
				continue
		# ERROR HANDLING
		if len(typing) >= 4:
			print("Max 3 types")
			typeInteraction()
		for _t in typing:	
			if _t not in CLEAR_TYPES:
				print(warningAnsi(f"\n{str(typing)} INVALID TYPE(S)!\n"))
				typeInteraction()
		
		# prettifing and managing the types for multiple types	
		if len(typing) == 3:
			weakness = prettify(list(set(flatten([weakTypes[typing[0]], weakTypes[typing[1]], weakTypes[typing[2]]]))))
			strengths = prettify(list(set(flatten([strongTypes[typing[0]], strongTypes[typing[1]], strongTypes[typing[2]]]))))
			multiInputTypes = f"{hexToAnsi(colors[typing[0].lower()], typing[0].upper())}, {hexToAnsi(colors[typing[1].lower()], typing[1].upper())} and {hexToAnsi(colors[typing[2].lower()], typing[2].upper())}"
		if len(typing) == 2:
			weaknesses = prettify(list(set(flatten([weakTypes[typing[0]], weakTypes[typing[1]]]))))
			strengths = prettify(list(set(flatten([strongTypes[typing[0]], strongTypes[typing[1]]]))))
			multiInputTypes = f"{hexToAnsi(colors[typing[0].lower()], typing[0].upper())} and {hexToAnsi(colors[typing[1].lower()], typing[1].upper())}"
		if len(typing) == 1:
			weakness = prettify(weakTypes[typing[0]])
			strengths = prettify(strongTypes[typing[0]])
			singleInputTypes = hexToAnsi(colors[typing[0].lower()], typing[0].upper())
		if len(typing) == 1:
			print(f"{singleInputTypes} is WEAK against: {weakness}")
			print(f"{singleInputTypes} is STRONG against: {strengths}")
		elif len(typing) == 2:
			print(f"{multiInputTypes} are WEAK against: {weaknesses}")
			print(f"{multiInputTypes} are STRONG against: {strengths}")
		elif len(typing) == 3:
			print(f"{multiInputTypes} are WEAK against: {weakness}")
			print(f"{multiInputTypes} are STRONG against: {strengths}")
		print()
typeInteraction()