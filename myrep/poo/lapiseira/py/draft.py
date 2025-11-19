class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.thickness = thickness
        self.hardness = hardness
        self.size = size
    
    def usage_per_sheet(self) -> int:
        if self.hardness == "HB" :
            return 1
        elif self.hardness == "2B" :
            return 2
        elif self.hardness == "4B" :
            return 4
        elif self.hardness == "6B" :
            return 6
        return 0
    
    def get_size(self) -> int:
        return self.size
    def get_thickness(self) -> float:
        return self.thickness
    def get_hardness(self) -> str:
        return self.hardness
    
    def set_size(self, size: int):
        self.size = size
    
    def __str__(self):
        return f"{self.thickness}:{self.hardness}:{self.size}"
    
class Pencil:
    def __init__(self, thickness: float):
        self.thickness = thickness
        self.tip: Lead | None = None
        self.barrel: list[Lead] = []

    def insert(self, lead: Lead) -> bool:
        if lead.get_thickness() != self.thickness :
            print ("fail: calibre incompatível")
            return False
        self.barrel.append(lead)
        return True
    
    def remove(self) -> Lead | None:
        if self.tip is None:
            print("fail: sem grafite no bico")
            return None
        removed = self.tip
        self.tip = None
        return removed
    
    def pull(self) -> bool:
        if self.tip is not None:
            print ("fail: já existe grafite no bico")
            return False
        if not self.barrel:
            print("fail:sem grafite no tambor")
            return False
        self.tip = self.barrel.pop(0)
        return True
    
    def write_page(self):
        if self.tip is None:
            print("fail: sem grafite no bico")
            return
        if self.tip.get_size() <= 10:
            print("fail: grfite acabou")
            self.tip = None
            return
        
        usage = self.tip.usage_per_sheet()
        if self.tip.get_size() - usage < 10:
            print("fail: folha incompleta")
            self.tip.set_size(10)
            return
        
        self.tip.set_size(self.tip.get_size() - usage)

def __str__(self):
    tip_str = str(self.tip) if self.tip else "null"
    barrel_str = ", ".join(str(lead) for lead in self.barrel)
    return f"Bico: {tip_str}\nTambor: [{barrel_str}]"
