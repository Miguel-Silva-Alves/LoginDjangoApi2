import requests

#==================get hello world========================

# headers = {'Authorization': 'Token 6523cf8a4982589f0693ab64c61908ad5bd74edd'}

# request = requests.get("http://127.0.0.1:8000/hello/", headers=headers)

# print(request.json())

#==================get token========================

# data = {'username': 'miguelsilvalves.2015@gmail.com', 'password': "minhasenha"}
# request = requests.post("http://127.0.0.1:8000/api-token-auth/", data=data)

# print(request.json())

#==================post user========================

# data = {'username': 'miguel_tes', 'password': "miguel12123", 'email':'miguel@teste.com', 'password_confirm':"miguel12123"}

# request = requests.post("http://127.0.0.1:8000/cadastrar_usuario/", data=data)

# print(request.json())

#===============get info with token=================
headers = {'Authorization': 'Token a7f2451dd67799a50921be0818e22044d17794be'}

request = requests.get("http://127.0.0.1:8000/requisicoes/", headers=headers)

print(request.json())