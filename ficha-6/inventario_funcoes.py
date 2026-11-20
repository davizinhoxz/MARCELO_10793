from time import sleep
from os import system

def meu_decorador(funcao):
    def wrapper(*args, **kwargs):
        funcao(*args, **kwargs)
        sleep(3)
        system("cls")
    return wrapper


@meu_decorador
def view(inventario):
    if len(inventario) == 0:
        print("Não há livros no inventário atual!")
    else:
        for livro in inventario:
            print(f"{livro["titulo"]} (Id {livro["id"]})")
            print(f"Autor: {livro["autor"]}; Stock: {livro["qtde"]}; Preço atual: {livro["preco"]}")
            print("-"*40)

def novo_id(inventario):
    if len(inventario) == 0:
        return 1
    return inventario[len(inventario)-1]["id"] + 1

@meu_decorador
def add(inventario: list):
    print("DADOS DO LIVRO\n")
    titulo = input("Título: ")
    autor = input("Autor: ")
    stock = int(input("Qtde atual: "))
    preco = float(input("Preço de venda: "))

    livro = {"id": novo_id(inventario), "titulo": titulo, "autor": autor, "qtde": stock, "preco": preco}
    inventario.append(livro)

@meu_decorador
def update_stock(inventario):
    found = False
    id_search = int(input("Digite o id do livro para atualização do stock: "))
    for livro in inventario:
        if livro["id"] == id_search:
            new_stock = int(input("Stock atual: "))
            livro["qtde"] = new_stock
            found = True
            break
    if not found:
        print("Não existe nenhum livro em stock com o id indicado")

@meu_decorador
def remove(inventario: list):
    found = False
    id_search = int(input("Digite o id do livro para remoção do inventário: "))
    for livro in inventario:
        if livro["id"] == id_search:
            inventario.remove(livro)
            found = True
            break
    if not found:
        print("Não existe nenhum livro em stock com o id indicado")

@meu_decorador
def search_by_author_or_title(inventario: list):
    found = False
    search = input("Digite o nome do livro ou do autor: ")
    for livro in inventario:
        autor: str = livro["autor"]
        titulo: str = livro["titulo"]
        if autor.find(search) >= 0 or titulo.find(search) >= 0:
            print(f"- {titulo} ({autor})")
            found = True
    if not found:
        print("Não existe nenhum livro em stock com o id indicado") 

@meu_decorador
def report(inventario):
    valor_inventario = 0
    for livro in inventario:
        valor_inventario += livro["qtde"] * livro["preco"]
    print(f"Valor atual do inventário: {round(valor_inventario,2)} euros")

def menu():
    print("GESTOR INVENTÁRIO\n")
    print("1- Visualizar inventário")
    print("2- Novo livro")
    print("3- Atualizar stock")
    print("4- Remover livro")
    print("5- Pesquisar livros por autor ou título")
    print("6- Valor atual em stock")
    print("7- Sair")
    op = int(input("\nEscolha uma opção: "))
    return op