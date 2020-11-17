import json

with open('bd.json', 'r') as arquivo_json:
    dic = json.load(arquivo_json)
    for chave,dados in dic.items():
        print(chave + ' | '+ str(dados))