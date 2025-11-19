class Person:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def __str__(self):
        return self.__name


class Market:
    def __init__(self, counter_count: int):
        self.counters: list[Person | None] = [None for _ in range(counter_count)]
        self.queue: list[Person] = []

    def __str__(self) -> str:
        counters_str = ", ".join("-----" if c is None else str(c) for c in self.counters)
        queue_str = ", ".join(str(p) for p in self.queue) if self.queue else "vazia"
        return f"Caixas: [{counters_str}]\nEspera: [{queue_str}]"

    def validate_index(self, index: int) -> bool:
        return 0 <= index < len(self.counters)

    def arrive(self, person: Person) -> None:
        self.queue.append(person)

    def call(self, index: int) -> bool:
        if not self.queue:
            print("fail: sem clientes")
            return False
        if not self.validate_index(index):
            print("fail: caixa inexistente")
            return False
        if self.counters[index] is not None:
            print("fail: caixa ocupado")
            return False

        self.counters[index] = self.queue.pop(0)
        return True

    def finish(self, index: int) -> Person | None:
        if not self.validate_index(index):
            print("fail: caixa inexistente")
            return None
        if self.counters[index] is None:
            print("fail: caixa vazio")
            return None

        client = self.counters[index]
        self.counters[index] = None
        return client

    
    def cut_in_line(self, sneaky: Person, gullible: str) -> bool:
        for i, p in enumerate(self.queue):
            if p.get_name() == gullible:
                self.queue.insert(i, sneaky)
                return True
        print("fail: pessoa alvo não encontrada")
        return False

    
    def give_up(self, quitter: str) -> bool:
        for i, p in enumerate(self.queue):
            if p.get_name() == quitter:
                self.queue.pop(i)
                return True
        print("fail: pessoa não encontrada na fila")
        return False
