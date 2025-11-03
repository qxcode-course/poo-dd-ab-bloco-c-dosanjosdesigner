
class Foo:
    def __init__(self, valor):
        self.valor = valor
        
    def __repr__(self):
        return f"Foo(valor={self.valor})"


lista_objeto = []
lista_objeto.append(Foo(10))

print(lista_objeto)


# lista_primitiva = []
# lista_primitiva.append ("a")
# #lista_primitiva.append ("b") 