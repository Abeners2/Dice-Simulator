# Arquivo dados.py dentro da pasta 'dados'

import random

def simular_lancamento_dados(numero_de_lancamentos):
    resultados = []
    for _ in range(numero_de_lancamentos):
        resultado = random.randint(1, 6)  # Gera um número aleatório entre 1 e 6 (faces de um dado)
        resultados.append(resultado)
    return resultados
