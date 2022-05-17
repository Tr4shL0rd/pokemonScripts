import json
import requests
from rich import print as rprint
pokeName = "charmander"
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
evoTwoName   = evoChainData["chain"]["evolves_to"][0]["species"]["name"]
evoThreeName = evoChainData["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]

print(f"{evoOneName} -> {evoTwoName} -> {evoThreeName}")
