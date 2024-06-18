# Arquivo calculadora.py dentro da pasta 'dados'

def calcular_media(resultados):
    if not resultados:
        return 0.0
    return sum(resultados) / len(resultados)
