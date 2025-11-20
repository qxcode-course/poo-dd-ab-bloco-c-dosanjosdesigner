class Kid:
    def __init__(self, name: str, age: int):
        self.name = name
        self.page = age

    def getName (self) -> str:
        return self.name
    
    def getAge(self) -> int:
        return self.age 
    def setName (self, name: str):
        self.name = name
    def setAge (self, age: int):
        self.age = age
    
    def __str__(self):
        return f"{self.name}:{self.age}"

class Trampoline:
    def __init__(self):
        self.playing: list[Kid] = []
        self.waiting: list[Kid] = []

    def arrive (self, kid: Kid):
        self.waiting.append(kid)

    def enter(self):
        if not self.waiting :
            print("fail: fila vazia")
            return
        self.playing.append(self.waiting.pop(0))

    def leave (self):
        if not self.playing:
            print("fail: ninguém no pula-pula")
            return
        self.waiting.append(self.playing.pop(0))


    def removeFromList(self, name: str, lst: list[Kid]) -> Kid | None:
        for i, kid in enumerate(lst):
            if kid.getName() == name:
                return lst.pop(i)
        return None

    
    def removeKid(self, name: str) -> Kid | None:
        kid = self.removeFromList(name, self.playing)
        if kid:
            return kid
        return self.removeFromList(name, self.waiting)

    def __str__(self):
        playing_str = ", ".join(str(kid) for kid in self.playing)
        waiting_str = ", ".join(str(kid) for kid in self.waiting)
        return f"Jogando: [{playing_str}]\nEsperando: [{waiting_str}]"


  
parquinho = Trampoline()
parquinho.arrive(Kid("Ana", 5))
parquinho.arrive(Kid("Beto", 6))
print(parquinho)  

parquinho.enter()
print(parquinho)  

parquinho.leave()
print(parquinho)  

