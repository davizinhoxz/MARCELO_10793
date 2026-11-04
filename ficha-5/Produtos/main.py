from functions import add, update_final_price

products = []

# def add(nome, preco, iva):
    
products.append(add("Camisa do Flamengo", 12.23, 0.13))

prd = input("Digite seu produto paezao: ")
pri = float(input("Digite o preço do produto: "))
iva = float(input("Iva do Produto: "))

products.append(add(prd,pri,iva))
