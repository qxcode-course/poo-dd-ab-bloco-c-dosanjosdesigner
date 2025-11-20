class Player:
    def __init__(self, label: int):
        self.label = label
        self.pos = 0
        self.free = True

    def getLabel(self) -> int:
        return self.label

    def getPos(self) -> int:
        return self.pos

    def setPos(self, pos: int):
        self.pos = pos

    def isFree(self) -> bool:
        return self.free

    def setFree(self, free: bool):
        self.free = free

    def __str__(self):
        return f"{self.label}:{self.pos}"


class Board:
    def __init__(self, nPlayers: int, boardSize: int):
        self.trapList: list[int] = []
        self.players: list[Player] = [Player(i+1) for i in range(nPlayers)]
        self.running = True
        self.boardSize = boardSize

    def addTrap(self, pos: int):
        if len(self.trapList) < 3:
            self.trapList.append(pos)

    def rollDice(self, value: int):
        for player in self.players:
            if not self.running:
                return

            if not player.isFree():
                if value % 2 == 0:
                    player.setFree(True)
                    print(f"Jogador {player.getLabel()} se libertou da armadilha!")
                else:
                    print(f"Jogador {player.getLabel()} continua preso.")
                continue

            newPos = player.getPos() + value
            if newPos > self.boardSize:
                print(f"Jogador {player.getLabel()} venceu!")
                self.running = False
                return

            player.setPos(newPos)
            if newPos in self.trapList:
                player.setFree(False)
                print(f"Jogador {player.getLabel()} caiu na armadilha!")

    def __str__(self):
        traps = ", ".join(map(str, self.trapList))
        players = ", ".join(str(p) for p in self.players)
        return f"Traps: [{traps}]\nPlayers: [{players}]"


#board = Board(2, 48) 
#board.addTrap(10)
#board.addTrap(20)
#board.addTrap(30)
#print(board)


#board.rollDice(7)  
#board.rollDice(5) 
#print(board)
