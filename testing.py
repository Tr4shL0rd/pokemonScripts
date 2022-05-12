from rich.console import Console
from rich.text import Text
console = Console()
def hexToRGB(hex):
    hex = hex.lstrip("#")
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
def hexToAnsi(hex,typename):
    rgb = hexToRGB(hex)
    ansi = "\033["
    ansi += f"38;2;{rgb[0]};{rgb[1]};{rgb[2]}" 
    ansi += "m"
    #ansi += hex
    ansi += typename
    ansi += "\033[0m"
    return ansi

#ansi format
#ESC[... 38;2;r;g;b...m]

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
normal   = hexToAnsi(colors["normal"],"Normal")
fire     = hexToAnsi(colors["fire"],"Fire")
water    = hexToAnsi(colors["water"],"Water")
electric = hexToAnsi(colors["electric"],"Electric")
grass    = hexToAnsi(colors["grass"],"Grass")
ice      = hexToAnsi(colors["ice"],"Ice")
fighting = hexToAnsi(colors["fighting"],"Fighting")
poison   = hexToAnsi(colors["poison"],"Poison")
ground   = hexToAnsi(colors["ground"],"Ground")
flying   = hexToAnsi(colors["flying"],"Flying")
psychic  = hexToAnsi(colors["psychic"],"Psychic")
bug      = hexToAnsi(colors["bug"],"Bug")
rock     = hexToAnsi(colors["rock"],"Rock")
ghost    = hexToAnsi(colors["ghost"],"Ghost")
dragon   = hexToAnsi(colors["dragon"],"Dragon")
dark     = hexToAnsi(colors["dark"],"Dark")
steel    = hexToAnsi(colors["steel"],"Steel")
fairy    = hexToAnsi(colors["fairy"],"Fairy")

print(normal)
print(fire)
print(water)
print(electric)
print(grass)
print(ice)
print(fighting)
print(poison)
print(ground)
print(flying)
print(psychic)
print(bug)
print(rock)
print(ghost)
print(dragon)
print(dark)
print(steel)
print(fairy)