# Arquivo sim_dados.py na raiz do projeto 'simulador_de_dados'

import random
from dados.calculadora import calcular_media  # Importa a função calcular_media do módulo calculadora

def simular_lancamento_dados(numero_de_lancamentos):
    resultados = []
    for _ in range(numero_de_lancamentos):
        resultado = random.randint(1, 6)  # Gera um número aleatório entre 1 e 6 (faces de um dado)
        resultados.append(resultado)
    return resultados

def main():
    print("Simulador de Lançamento de Dados")
    numero_de_lancamentos = int(input("Quantos lançamentos de dados você deseja simular? "))
    
    resultados = simular_lancamento_dados(numero_de_lancamentos)
    
    print("\nResultados dos lançamentos:")
    for i, resultado in enumerate(resultados, start=1):
        print(f"Lançamento {i}: {resultado}")
    
    media = calcular_media(resultados)
    print(f"\nMédia dos resultados: {media:.2f}")

if __name__ == "__main__":
    main()
