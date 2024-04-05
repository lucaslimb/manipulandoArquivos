from Functions import *

inventario = {}

escolha = menu()

while escolha == 1 or escolha == 2 or escolha == 3:
    if escolha == 1:
        registrar(inventario)
    if escolha == 2:
        gerarArquivo(inventario)
    if escolha == 3:
        resultado = exibirArquivo()
        for linha in resultado:
            lista = linha.split(";")
            print("Data: {} / Descrição: {} / Departamento: {}"
                  .format(lista[1],
                                lista[2],
                                lista[3]))
    escolha = menu()