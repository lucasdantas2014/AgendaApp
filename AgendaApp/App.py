import json


continuar = True
while(continuar):
    try:
        f = open("meses.txt",encoding= "utf-8")
        linhas = f.readlines()
        for linha in linhas:
            print(linha.strip())
        continuar = False

    except FileNotFoundError:
        print("Arquivo não encontrado")





