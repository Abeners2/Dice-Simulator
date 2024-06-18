import random

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

if __name__ == "__main__":
    main()
