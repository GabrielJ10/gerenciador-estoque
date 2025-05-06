
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
