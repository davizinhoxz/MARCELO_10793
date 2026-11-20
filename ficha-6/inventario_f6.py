from inventario_funcoes import *
from time import sleep
from os import system
livros = []

while True:
    op = menu()
    match op:
        case 1:
            view(livros)
            sleep(5)
            system("cls")
        case 2:
            add(livros)
            sleep(5)
            system("cls")
        case 3:
            update_stock(livros)
            sleep(5)
            system("cls")
        case 4:
            remove(livros)
            sleep(5)
            system("cls")
        case 5:
            search_by_author_or_title(livros)
            sleep(5)
            system("cls")
        case 6:
            report(livros)
            sleep(5)
            system("cls")
        case 7:
            break

print("Aplicação finalizada!")
    
