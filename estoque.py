
class Produto:
    def __init__(self, nome: str, preco: float, qtd: int):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def __str__(self):
        return f"Produto(nome={self.nome}, preco={self.preco:.2f}, qtd={self.qtd})"

estoque: list[Produto] = []

def adicionar_produto(prod: Produto):
    estoque.append(prod)

def remover_produto(nome_alvo: str) -> bool:
    for i, prod in enumerate(estoque):
        if prod.nome == nome_alvo:
            estoque.pop(i)
            return True
    return False

for indice, produto in enumerate(estoque):
    nome_produto = produto.nome  # variável explicativa
    if nome_produto == nome_alvo:
        estoque.pop(indice)
        return True
