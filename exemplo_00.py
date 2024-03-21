import requests

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/15")
data = response.json()
# Supondo que 'data' é o dicionário com os dados do Pokémon
data_types = data['types']
types_list = []
for type_info in data_types:
    types_list.append(type_info['type']['name'])
types = ', '.join(types_list)
print(data_types)
print(types_list)
print(types)
print(data['name'])
print(data['name'], types)

lista_exemplo = ["luciano", "fabio", "bruno"]
lista_unica = ', '.join(lista_exemplo)
print(lista_unica)
