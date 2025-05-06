# Projeto 3: Gerenciador de Estoque
produtos = []

def adicionar():
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    qtd = int(input("Qtd: "))
    produtos.append({"nome": nome, "preco": preco, "qtd": qtd})
    print("Adicionado!")

def remover():
    n = input("Nome a remover: ")
    for i in range(len(produtos)):
        if produtos[i]["nome"] == n:
            produtos.pop(i)
            print("Removido!")
            return
    print("Não encontrado")

def mostrar():
    for p in produtos:
        print("Nome:", p["nome"])
        print("Preço:", p["preco"])
        print("Qtd:", p["qtd"])

while True:
    print("1-Adicionar 2-Remover 3-Mostrar 4-Sair")
    op = input("Opção: ")
    if op == "1":
        adicionar()
    elif op == "2":
        remover()
    elif op == "3":
        mostrar()
    elif op == "4":
        break