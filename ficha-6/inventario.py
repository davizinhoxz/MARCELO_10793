from inventario_funcoes import *

livros = []

while True:
    op = menu()
    match op:
        case 1:
            view(livros)
        case 2:
            add(livros)
        case 3:
            update_stock(livros)
        case 4:
            remove(livros)
        case 5:
            search_by_author_or_title(livros)
        case 6:
            report(livros)
        case 7:
            break

print("Aplicação finalizada!")
    
