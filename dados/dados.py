import random

def simular_lancamento_dados(numero_de_lancamentos, faces):
    resultados = []
    for _ in range(numero_de_lancamentos):
        resultado = random.randint(1, faces) 
        resultados.append(resultado)
    return resultados
