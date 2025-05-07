from estoque import Produto, adicionar_produto, remover_produto, estoque

def ler_dados_produto() -> Produto:
    try:
        nome = input("Nome: ").strip()
        preco = float(input("Preço: "))
        qtd = int(input("Qtd: "))
    except ValueError as e:
        print("Valor inválido. Reinicie a operação.")
        raise

    if preco < 0 or qtd < 0:
        raise ValueError("Preço e quantidade não podem ser negativos.")
    return Produto(nome, preco, qtd)

def adicionar_produto_ui():
    prod = ler_dados_produto()
    adicionar_produto(prod)
    print("Produto adicionado com sucesso!")

def remover_produto_ui():
    nome_alvo = input("Nome do produto a remover: ")
    sucesso = remover_produto(nome_alvo)
    print("Removido!" if sucesso else "Produto não encontrado")

def listar_estoque_ui() -> None:
    if not estoque:
        print("Estoque vazio.")
    else:
        print("\n-- Lista de Produtos --")
        for produto in estoque:
            print(produto)

def mostrar_menu() -> str:
    print("\n=== Gerenciador de Estoque ===")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Listar estoque")
    print("4 - Sair")
    return input("Escolha uma opção: ").strip()
