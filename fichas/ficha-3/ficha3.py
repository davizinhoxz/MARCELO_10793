lista = [1,2,3,4,5,6,7,8,9,10]

# multi = []
# maiuscula = []
# maiores = []
# lista_palavras = ["arantini", "pastel", "triste das ia", "costa"]
# quadrados = []
# pares = []
frutas = ["Banana","Maca","Morango", "Uva", "Pessego"]

# ex1
# pares = [num for num in lista if num % 2 == 0]
# print(pares)

# ex2
# for num in lista:
#     quadrados.append(num **2)
# print(quadrados)

# ex3
# letras_palavras = [len(size) for size in lista_palavras]
# print(letras_palavras)

# ex4
# maiores = [num for num in lista if num > 5]
# print(maiores)

# ex5
# nome = 'MarcelO ViEiRa amorIM'
# for letra in nome:
#      if letra == letra.upper() and " " != letra.upper():
#         maiuscula.append(letra)
# print(maiuscula)

# ex6
# multi = [num*2 if num % 3 == 0 else num for num in lista]
# print(multi)

# ex7
# inicialA = [palavra.upper() for palavra in lista_palavras if palavra.startswith("A")]

# ex8
tamanhoFrutas = [len(fruta) if len(fruta) > 5 else 0 for fruta in frutas]
print(tamanhoFrutas)