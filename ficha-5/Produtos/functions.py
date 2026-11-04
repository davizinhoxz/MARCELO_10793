# Crie uma função que receba o nome do produto, o preço e o iva e guarde a
# informação em um dicionário onde as chaves serão product, price e tax. A função
# deve ser denominada add.


def add(nome, preco: float, iva: float):
    return {
        "product": nome,
        "price": preco,
        "tax": iva
    }
    

def update_final_price(d):
    d["final_price"] = round(d["price"] * (1 + d["tax"]),2)


def print_products(d):
    return f"O produto {d["product"]} com preço de {d["price"]} e iva de {d["tax"]*100}%"


def menu():
        print("----------SISTEMA-DE-PRODUTOS----------")
        print("1. Inserir um novo produto")
        print("2. Listar os produtos existentes")
        print("3. Atualizar o preço final de todos os produtos")
        print("4. Imprimir os dados de um produto específico")
        print("5. Terminar a aplicação")
        
        op = input("Escolha uma opção (1-5): ")
        return op 


def print_Product(productName, list):
    for product in list:
         if productName == product["product"]:
            return f"O produto {product["product"]} com preço de {product["price"]} e iva de {product["tax"]*100}%"