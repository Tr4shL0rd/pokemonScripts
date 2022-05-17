from itertools import chain
import json
import requests
from rich import print as rprint

def chaining(evos:list):
    for i in range(len(evos)):
        for elem in evos:
            if elem == "None":
                evos.remove(elem)
    if len(evos) == 3:
        return f"{evos[0]} -> {evos[1]} -> {evos[2]}"
    elif len(evos) == 2:
        return f"{evos[0]} -> {evos[1]}"
    elif len(evos) == 1:
        return f"{evos[0]}"
pokeName = "pinsir"
url = f"https://pokeapi.co/api/v2/pokemon/{pokeName}/"
r = requests.get(url)
data = r.json()

speciesUrl = data["species"]["url"]
r = requests.get(speciesUrl)
speciesData = r.json()

evoChain = speciesData["evolution_chain"]["url"]
r = requests.get(evoChain)
evoChainData = r.json()

evoOneName   = pokeName
try:
    evoTwoName   = evoChainData["chain"]["evolves_to"][0]["species"]["name"]
except IndexError:
    evoTwoName   = "None"
try:
    evoThreeName = evoChainData["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]
except IndexError:
    evoThreeName   = "None"
evos = []
evos.append(evoOneName)
evos.append(evoTwoName)
evos.append(evoThreeName)
print(chaining(evos))
#print(f"{evos[0]} -> {evos[1]} -> {evos[2]}")
