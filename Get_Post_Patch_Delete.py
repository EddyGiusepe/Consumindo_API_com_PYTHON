# Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro 
# Exemplo baseado no link: https://www.youtube.com/watch?v=IdviYZIQLlA
# Meu banco de Dados (gmail Eddy): https://console.firebase.google.com/project/teste-6bb33/database/teste-6bb33-default-rtdb/data

print("######################################")
print("## Biblioteca requets (REQUISIÇÕES)  ##")
print("######################################")
print("")
# Temos as seguintes requisições:
# GET --> Pegar informações do banco de Dados (para nosso caso)
# POST --> Criar uma nova informação (inserir uma nova informaçao)
# PATCH --> Editar uma informação (atualizar uma informação)
# DELETE --> Deletar informações



print("####################")
print("## Exemplo_1: GET ##")
print("####################")
print("")
# Importamos as nossa Biblioteca
import requests
print("O site na qual fazemos um GET é: https://docs.awesomeapi.com.br/api-de-moedas")
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

print("A requisição será um número (entre 200-299) que significa que DEU CERTO: {}".format(requisicao))
print("")
print("Agora vamos ver essa informação no formato .json (no Python seria um dicionário): ")
print(requisicao.json())
print("")


print("####################")
print("## Exemplo_2: GET ##")
print("####################")
print("")
# Neste exemplo utilizaremos o site: firebase (banco de Dados da Google)
print("O site na qual fazemos um GET é: https://firebase.google.com/?gclid=CjwKCAjw-ZCKBhBkEiwAM4qfFyeyBBgjFYhdCtNYCNJDutYtDh6cUQWdrIFkMguRH6F-9Hv9RxmtsxoC04YQAvD_BwE&gclsrc=aw.ds")
requisicao = requests.get("https://teste-6bb33-default-rtdb.firebaseio.com/.json") # No final adicionei .json porque a página fala isso

print("A requisição será um número (entre 200-299) que significa que DEU CERTO: {}".format(requisicao))
print("")
print("Agora vamos ver essa informação no formato .json (no Python seria um dicionário): ")
print(requisicao.json())
print("")



print("####################")
print("## Exemplo_3: POST ##")
print("####################")
print("")
# Neste exemplo seguiremos utilizando o site: firebase (banco de Dados da Google)
Dados_inseridos = '[ { "Nome" : "Eddy Giusepe Chirinos Isidro"}, { "Nome" : "Katty Verónica Chirinos Isidro"} ]' # Tem que ser um .json dentro de aspas simples
requisicao = requests.post("https://teste-6bb33-default-rtdb.firebaseio.com/.json", data=Dados_inseridos)
print("Agora vamos ver a response: ")
print(requisicao)
print(requisicao.json())
print("")


print("######################")
print("## Exemplo_4: PATCH ##")
print("######################")
print("")
# Neste exemplo seguiremos utilizando o site: firebase (banco de Dados da Google)
Atualizando_Dados = '{ "Nome": "Eddy Giusepe", "Profissão": "Data Scientist Jr." }' # Tem que ser um .json dentro de aspas simples
requisicao = requests.patch("https://teste-6bb33-default-rtdb.firebaseio.com/-Mjr8mAc4yRJgyzhM547/0/Nome.json", data= Atualizando_Dados) # Peguei o link, lá do campo a modificar
print("Agora vamos ver a response: ")
print(requisicao)
print(requisicao.json())
print("")


print("#######################")
print("## Exemplo_5: DELETE ##")
print("#######################")
print("")
# Neste exemplo seguiremos utilizando o site: firebase (banco de Dados da Google)

deletar = requests.delete("https://teste-6bb33-default-rtdb.firebaseio.com/-MjrAtNPUuhOBR8eojvG/0/Nome.json") # Peguei o link de lá... para poder deletar
print("Agora vamos ver a response: ")
print(deletar)
print(deletar.json())
print("")



