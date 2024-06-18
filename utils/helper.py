# Arquivo helper.py dentro da pasta 'utils'

def formatar_resultados(resultados):
    formatted_result = "\n".join([f"Lançamento {i + 1}: {resultado}" for i, resultado in enumerate(resultados)])
    return formatted_result
