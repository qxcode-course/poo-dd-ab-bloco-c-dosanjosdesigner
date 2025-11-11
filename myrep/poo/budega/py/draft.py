class Cliente : 
    def __init__(self, nome: str):
        self.__nome = nome

        
    def getNome (self) -> str:
        return self.__nome
    
    def __str__(self):
        return f"{self.__nome}"
    
class Market:
    def __init__(self, qtd_caixas: int):
        self.caixas = [None for _ in range(qtd_caixas)]
        self.espera = []

    def __str__(self) -> str:
        caixas_str = ", ".join(map(lambda c: "-----" if c is None else c, self.caixas))
        espera_str =  ", ".join(self.espera) if self.espera else "vazia"
        return f"Caixas: {caixas_str}]\nEspera: [{espera_str}]" 
