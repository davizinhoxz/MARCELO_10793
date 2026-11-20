class Cliente:
    # Atributos da classe
    total_clientes = 0
    def __init__(self,nome,peso,altura):
        # Atributos da instância
        self.nome = nome
        self.peso = peso
        self.altura = altura

    #Metodos Especiais
    # def __str__(self):
    #     return f"O(A) cliente {c1.nome} tem {c1.altura}cm e pesa {c1.peso}Kg"
    
    # def __eq__(self, c1):
    #     return self.nome == c1.nome
        

    # Metodo da classe
    @classmethod
    def procurar(cls, cliente_a_pesquisar):
        if cliente_a_pesquisar == "ana":
            return True
        return False


c1 = Cliente("Tomas Rompante",69,1.76)
c2 = Cliente("Maria Moreira 67",67,1.67)
c3 = Cliente("Leonor",59,1.64)
lista = [c2,c2,c3]


if c1 == c2:
    print("ok")
if c2 == c3:
    print("Segundo ok")
    
    
print(f"Total de Clientes: {Cliente.total_clientes}")


for c in lista:
    if Cliente.procurar(c.nome):    
        print(c)


# print(f"O(A) cliente {c1.nome} tem {c1.altura}cm e pesa {c1.peso}Kg")
print(f"O(A) cliente {c1.nome} tem {c1.altura}cm e pesa {c1.peso}Kg tem gosto pela {c2.nome} que tem {c2.altura}cm e pesa {c2.peso}Kg ")