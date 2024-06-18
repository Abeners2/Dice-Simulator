# Arquivo dados.py dentro da pasta 'dados'

import random

def simular_lancamento_dados(numero_de_lancamentos, faces):
    resultados = []
    for _ in range(numero_de_lancamentos):
        resultado = random.randint(1, faces)  # Gera um número aleatório entre 1 e o número de faces do dado
        resultados.append(resultado)
    return resultados
