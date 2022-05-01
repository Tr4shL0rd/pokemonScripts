import requests
import json
import sys

def prettifyArrOutput(arr):
    string = ""
    if len(arr) == 1:
        return arr[0].title()
    if len(arr) == 2:
        return f"{arr[0].title()} and {arr[1].title()}"
    for i,elem in enumerate(arr):
        if elem == arr[-1]:
            string += f"and {arr[-1].title()}"
            break
        string += f"{elem.title()}, "
    return string
## Base data like the Pokemon names...

## Type interaction data
def interactionData(type:str, strong=True, weak=False):
    """
    if no params except type are given, it will return a tuple of 2 elements containing the strong and weak types
    if strong is set to True, it will return a tuple of 1 elements containing the Strong againts types
    if weak is set to True, it will return a tuple of 1 elements containing the Weak againts types
    else it'll return a tuple of 2 elements containing the Strong againts types and Weak againts types
    """
    typeNames = ["normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison",
            "ground", "flying", "psychic", "bug", "rock", "ghost", "dark", "dragon", "steel", "fairy"]

    type = type.lower().strip()
    
    typesUrl =   f"https://pokeapi.co/api/v2/type/{type}"
    pokemonTypeInteractionRequest = requests.get(typesUrl)
    pokemonTypeInteractionData = json.loads(json.dumps(pokemonTypeInteractionRequest.json(), indent=4))
    data = None
    if strong:
        damToArr  = []
        damTo = pokemonTypeInteractionData["damage_relations"]["double_damage_to"]
        for i in range(len(damTo)):
            damToArr.append(damTo[i]["name"])
        data = damToArr
        print(f"{type.title()} Is Strong against {prettifyArrOutput(data)}")
    if weak:
        damFromArr = []
        damFrom = pokemonTypeInteractionData["damage_relations"]["double_damage_from"]
        for i in range(len(damFrom)):
            damFromArr.append(damFrom[i]["name"])  
        data = damFromArr
        print(f"{type.title()} Is weak against {prettifyArrOutput(data)}")
    return data
def getType(name:str):
    """
    This function will return the type of a pokemon
    """
    name = name.lower().strip()
    pokemonUrl = f"https://pokeapi.co/api/v2/pokemon/{name}"
    pokemonRequest = requests.get(pokemonUrl)
    pokemonData = json.loads(json.dumps(pokemonRequest.json(), indent=4))
    return pokemonData["types"][0]["type"]["name"]



#typeNames = ["normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison",
#            "ground", "flying", "psychic", "bug", "rock", "ghost", "dark", "dragon", "steel", "fairy"]
typing = input("Please Enter Pokemon Type: ").lower().strip()
#if typing not in typeNames:
#    print("Type not found")
#    exit()

pokemonUrl = "https://pokeapi.co/api/v2/pokemon/charmander"
pokemonBaseRequest = requests.get(pokemonUrl)
pokemonBaseData = json.loads(json.dumps(pokemonBaseRequest.json(), indent=4))
name = pokemonBaseData["name"]
pokedexId = pokemonBaseData["id"]

types = []
for i in range(len(pokemonBaseData["types"])):
    types.append(pokemonBaseData["types"][i]["type"]["name"])
interactionData(typing, weak=True)
#print(getType(pokeName))
#arr = ["abe","kat","mus"]
#prettifyArrOutput(arr)