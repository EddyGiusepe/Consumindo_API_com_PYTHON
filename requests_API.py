# Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro

# Links de estudos:
# https://www.youtube.com/watch?v=vrIQM8257Zc
# https://www.youtube.com/watch?v=IdviYZIQLlA
import requests
import os

# A seguir: o comando limpa o terminal depois de rodar o Script
# os.system('clear')

print("######################################")
print("## Dados respeito ao CEP solicitado ##")
print("######################################")
print("")
cep = input("Digite o CEP (número de apenas 8 dígitos):")
r = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))

data = r.json()
print("Aqui imprimimos o .json total: ")
print(data)

print("")
print("CEP: {}".format(data["cep"]))
print("Logradouro: {}".format(data["logradouro"]))
print("Bairro: {}".format(data["bairro"]))
print("Localidade: {}".format(data["localidade"]))
print("UF: {}".format(data["uf"]))
print("")

