def menu():
    opcao = int(input("Digite: \n1 para registrar ativo "
                      "\n2 para persistir em arquivo"
                      "\n3 para exibir ativos armazenados\n"))
    return opcao

def registrar(inventario):
        resp = "S"
        while resp == "S":
            inventario[input("Digite o número patrimonial: ")]=[
                input("Digite a data da última atualização: "),
                input("Digite a descrição: "),
                input("Digite o departamento: ")]
            resp = input("Digite S para continuar.").upper()

def gerarArquivo(inventario):
        with open("inventario.csv", "a") as inv:
            for chave, valor in inventario.items():
                inv.write("{};{};{};{}\n" .format(chave, valor[0], valor[1], valor[2]))
        print("Arquivo gerado com sucesso!")

def exibirArquivo():
        with open("inventario.csv", "r") as inv:
           linhas = (inv.readlines())
        return linhas