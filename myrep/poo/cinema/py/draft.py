class Client:
    def __init__(self, id: str, phone: int):
        self.id = id
        self.phone = phone

    def getId(self) -> str:
        return self.phone
    
    def setId(self, id: str):
        self.id = id

    def setPhone(self, phone: int):
        self.phone = phone

    def setPhone(self,phone: int):
        self.phone = phone

    def __str__(self):
        return f"{self.id}:{self.phone}"
    

class Theater:
    def __init__(self, capacity: int):
        self.seats: list[Client | None] = [None for _ in range(capacity)]

    def verifyIndex(self, index: int) -> bool:
        return 0 <= index < len(self.seats)

    def search(self, name: str) -> int:
        for i, client in enumerate(self.seats):
            if client and client.getId() == name:
                return i
        return -1

    def reserve(self, id: str, phone: int, index: int) -> bool:
        if not self.verifyIndex(index):
            print("fail: cadeira inexistente")
            return False
        if self.seats[index] is not None:
            print("fail: cadeira ocupada")
            return False
        if self.search(id) != -1:
            print("fail: cliente já está na sala")
            return False

        self.seats[index] = Client(id, phone)
        return True

    def cancel(self, id: str) -> bool:
        pos = self.search(id)
        if pos == -1:
            print("fail: cliente não encontrado")
            return False
        self.seats[pos] = None
        return True

    def getSeats(self) -> list[Client | None]:
        return self.seats

    def __str__(self):
        return "[" + " ".join(str(c) if c else "-" for c in self.seats) + "]"


sala = Theater(5)
print(sala)  
sala.reserve("ana", 1234, 0)
sala.reserve("bob", 5678, 2)
print(sala)  
sala.cancel("ana")
print(sala) 

        