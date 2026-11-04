def add(produto, preco, iva=0.23):
    return {
        "product": produto,
        "price": preco,
        "tax": iva
    }

def update_final_price(d):
    d["final_price"] = d["price"] * (1 + d["tax"])
