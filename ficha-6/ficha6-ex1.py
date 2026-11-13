def view(inventario):
    if len(inventario) == 0:
        print("Não ha livros no meu inventario")
    for livro in inventario:
        print(f"")