titulos = []

biblioteca = {
    "livro1": {
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "ano": 2015,
        "disponivel": True
    },
    "livro2": {
        "titulo": "Pense em Python",
        "autor": "Allen B. Downey",
        "ano": 2012,
        "disponivel": False
    },
    "livro3": {
        "titulo": "Introdução à Programação com Python",
        "autor": "Nilo Ney Coutinho Menezes",
        "ano": 2019,
        "disponivel": True
    }
}

for livro in biblioteca.values():
    if livro["disponivel"] == True:
         print(livro["titulo"])
         if livro["autor"] == "Luciano Ramalho":
              titulos.append(livro["titulo"])


biblioteca["livro4"] = {
        "titulo": "Portugol;",
        "autor": "David DaCosta",
        "ano": 2026,
        "disponivel": True
}

biblioteca["livro1"]["disponivel"] = False


print(f"Titulo dos livros escritos por Luciano Ramalho: {titulos} ")