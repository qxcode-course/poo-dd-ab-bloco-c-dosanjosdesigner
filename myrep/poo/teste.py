valores: dict[str, int] = {
    "um": 1,
    "dois": 2,
    "tres": 3,
    "quatro": 4,
    "cinco": 5,
    "seis": 6
}

nomes: dict[int, str] = {
    1: "um",
    2: "dois",
    3: "tres",
    4: "quatro",
    5: "cinco",
    6: "seis"
}

def somar(a: str, b: str) -> str:
    ##Pegar os valores numéricos
    valor_a = valores[a]
    valor_b = valores[b]

    ##Somar
    resultado = valor_a + valor_b

    ##Converter para palavra
    return nomes[resultado]

#Testes
print(somar("um", "um"))      
print(somar("um", "dois"))    
print(somar("dois", "dois"))  