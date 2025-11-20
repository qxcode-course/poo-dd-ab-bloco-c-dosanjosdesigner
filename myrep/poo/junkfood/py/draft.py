class Slot:
    def __init__(self, name: str = "empty", price: float = 0.0, quantity: int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getName(self) -> str:
        return self.name

    def getPrice(self) -> float:
        return self.price

    def getQuantity(self) -> int:
        return self.quantity

    def setName(self, name: str):
        self.name = name

    def setPrice(self, price: float):
        self.price = price

    def setQuantity(self, quantity: int):
        self.quantity = quantity

    def __str__(self):
        return f"[ {self.name} : {self.quantity} U : {self.price:.2f} RS]"


class VendingMachine:
    def __init__(self, capacity: int):
        self.slots: list[Slot] = [Slot() for _ in range(capacity)]
        self.cash = 0.0
        self.profit = 0.0
        self.capacity = capacity

    def verifyIndex(self, index: int) -> bool:
        return 0 <= index < self.capacity

    def getSlot(self, index: int) -> Slot:
        if not self.verifyIndex(index):
            print("fail: indice nao existe")
            return None
        return self.slots[index]

    def setSlot(self, index: int, name: str, qtd: int, price: float):
        if not self.verifyIndex(index):
            print("fail: indice nao existe")
            return
        self.slots[index].setName(name)
        self.slots[index].setQuantity(qtd)
        self.slots[index].setPrice(price)

    def clearSlot(self, index: int):
        if not self.verifyIndex(index):
            print("fail: indice nao existe")
            return
        self.slots[index] = Slot()

    def insertCash(self, value: float):
        self.cash += value

    def withdrawCash(self) -> float:
        troco = self.cash
        self.cash = 0.0
        return troco

    def buyItem(self, index: int):
        if not self.verifyIndex(index):
            print("fail: indice nao existe")
            return
        slot = self.slots[index]
        if slot.getQuantity() == 0:
            print("fail: espiral sem produtos")
            return
        if self.cash < slot.getPrice():
            print("fail: saldo insuficiente")
            return
        
        slot.setQuantity(slot.getQuantity() - 1)
        self.cash -= slot.getPrice()
        self.profit += slot.getPrice()

    def getCash(self) -> float:
        return self.cash

    def getProfit(self) -> float:
        return self.profit

    def __str__(self):
        slots_str = " ".join(str(slot) for slot in self.slots)
        return f"Saldo: {self.cash:.2f} RS\n{slots_str}"