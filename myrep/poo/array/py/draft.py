
class Foo:
    def __init__(self, valor):
        self.valor = valor
        
    def __repr__(self): # preciso deste metodo pois preciso imprimir diretamente o objeto e se não tiver por padrão o pyton mostra o endereço de memória do objeto e não o conteúdo.
        return f"Foo(valor={self.valor})"


lista_objeto = []
lista_objeto.append(Foo(10))

print(lista_objeto)


# lista_primitiva = []
# lista_primitiva.append ("a")
# #lista_primitiva.append ("b") 