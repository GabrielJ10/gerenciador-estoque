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

def remover_produto_ui():
    nome_alvo = input("Nome do produto a remover: ")
    sucesso = remover_produto(nome_alvo)
    print("Removido!" if sucesso else "Produto não encontrado")

def listar_estoque():
    from estoque import estoque
    for produto in estoque:
        print(produto)  # usa __str__ de Produto