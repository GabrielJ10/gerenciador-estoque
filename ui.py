from estoque import Produto

def ler_dados_produto() -> Produto:
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    qtd = int(input("Qtd: "))
    return Produto(nome, preco, qtd)

def adicionar_produto_ui():
    prod = ler_dados_produto()
    adicionar_produto(prod)
    print("Produto adicionado com sucesso!")