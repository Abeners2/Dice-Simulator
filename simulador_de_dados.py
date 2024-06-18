from dados.dados import simular_lancamento_dados 
from dados.calculadora import calcular_media 
from utils.helper import formatar_resultados 

def main():
    print("Simulador de Lançamento de Dados")
    numero_de_lancamentos = int(input("Quantos lançamentos de dados você deseja simular? "))
    
    faces = int(input("Quantas faces o dado deve ter? "))
    
    resultados = simular_lancamento_dados(numero_de_lancamentos, faces)
    
    print("\nResultados dos lançamentos:")
    print(formatar_resultados(resultados))
    
    media = calcular_media(resultados)
    print(f"\nMédia dos resultados: {media:.2f}")

if __name__ == "__main__":
    main()
