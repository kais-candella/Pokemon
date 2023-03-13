import json

#PA = Puissance d'attaque 
pokemon_1 = """{
    "name"              : "Dracaufeu",
    "PV"                : 125,
    "Defense"           : 25,
    "PA"                : 25, 
    "type"              : ["Feu" , "Eau" , "Psy" , "Normal"]
}"""

pokemon_2 = """{
    "name"              : "Tortank",
    "PV"                : 125,
    "Defense"           : 25,
    "PA"                : 25, 
    "type"              : ["Feu" , "Eau" , "Psy" , "Normal"]
}"""


pokemon_3 = """{
    "name"              : "Mewtwo",
    "PV"                : 150,
    "Defense"           : 20,
    "PA"                : 40, 
    "type"              : ["Feu" , "Eau" , "Psy" , "Normal"]
}"""


pokemon_4 = """{
    "name"              : "Évoli",
    "PV"                : 100,
    "Defense"           : 20,
    "PA"                : 15, 
    "type"              : ["Feu" , "Eau" , "Psy" , "Normal"]
}"""

pokemon_5 = """{
    "name"              : "Ectoplasma",
    "PV"                : 150,
    "Defense"           : 23,
    "PA"                : 30, 
    "type"              : ["Feu" , "Eau" , "Psy" , "Normal" , "Spectre" , "Poisson" ]
}"""

convert_json = json.loads(pokemon_1)
print(convert_json['name'], convert_json['type'][0],convert_json['Defense'], convert_json['PA'],convert_json['PV'])

convert_json = json.loads(pokemon_2)
print(convert_json['name'], convert_json['type'][1],convert_json['Defense'], convert_json['PA'], convert_json['PV'])

convert_json = json.loads(pokemon_3)
print(convert_json['name'], convert_json['type'][2],convert_json['Defense'], convert_json['PA'], convert_json['PV'])

convert_json = json.loads(pokemon_4)
print(convert_json['name'], convert_json['type'][3],convert_json['Defense'], convert_json['PA'], convert_json['PV'])

convert_json = json.loads(pokemon_5)
print(convert_json['name'], convert_json['type'][4] , convert_json['type'][5]  ,convert_json['Defense'], convert_json['PA'], convert_json['PV'])



with open('Pokedexdata.json', 'w') as json_file:
    data = json.dump(convert_json, json_file, indent=4)

