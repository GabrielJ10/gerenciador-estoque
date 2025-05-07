from ui import (
    mostrar_menu,
    adicionar_produto_ui,
    remover_produto_ui,
    listar_estoque_ui
)

def main() -> None:
    while True:
        opcao = mostrar_menu()
        if opcao == "1":
            adicionar_produto_ui()
        elif opcao == "2":
            remover_produto_ui()
        elif opcao == "3":
            listar_estoque_ui()
        elif opcao == "4":
            print("Encerrando o Gerenciador de Estoque. Até breve!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()