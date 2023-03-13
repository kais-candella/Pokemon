import json

class Création:

    def __init__(self, nom, type):
        self.nom = nom
        self.type = type

    def get_nom_pokemon(self):
        return self.nom

    def set_nom_pokemon(self, nom):
        self.nom = nom

    def get_type_pokemon(self):
        return self.type

    def set_type_pokemon(self, type):
        self.type = type

with open('statspokemon.json') as f:
    statspokemon = json.load(f)

création = Création("", "")

création.set_nom_pokemon(input("Quel sera le nom de ton Pokemon ? "))

type_pokemon = ""
while type_pokemon not in statspokemon:
    type_pokemon = input("Quel sera le type de ton Pokemon ? parmis cette liste [Feu, Eau, Spectre, Normal, Poison, Psy] ")
    if type_pokemon not in statspokemon:
        print("Type de Pokémon invalide")

stats = statspokemon[type_pokemon]

print("Ton Pokémon", création.get_nom_pokemon(), "est prêt au combat!")
print("il sera de type :", type_pokemon)
print("PV:", stats["PV"])
print("Défense:", stats["Defense"])
print("PA:", stats["PA"])