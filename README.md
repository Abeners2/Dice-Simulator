# Simulador de Lançamento de Dados

## Descrição
Este projeto implementa um simulador de lançamento de dados em Python. Ele permite ao usuário simular o lançamento de um dado com um número específico de faces várias vezes, calcular a média dos resultados e exibir os resultados formatados.

## Instalação
Para executar este programa localmente, siga os passos abaixo:

## Clone o repositório:
```bash
git clone https://github.com/Abeners2/Dice-Simulator
```

## Navegue até o diretório do projeto:

```bash
cd Dice-Simulator
```

## Execute o programa:

```bash
python simulador_de_dados.py
```

## Uso
Ao executar o programa, você será solicitado a inserir o número de lançamentos desejado e o número de faces do dado. O programa então simula os lançamentos, exibe os resultados formatados e calcula a média dos resultados.

### Explicação dos Arquivos

#### simulador_de_dados.py
O arquivo simulador_de_dados.py contém a função principal que inicia o programa de simulação de lançamento de dados. Ele solicita ao usuário o número de lançamentos desejado e o número de faces do dado, simula os lançamentos, exibe os resultados formatados e calcula a média dos resultados.

```python
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
```

#### calculadora.py
O arquivo calculadora.py define a função calcular_media, que calcula a média dos valores em uma lista de resultados. Se a lista estiver vazia, a função retorna 0.0.

```python
def calcular_media(resultados):
    if not resultados:
        return 0.0
    return sum(resultados) / len(resultados)
```

#### dados.py
O arquivo dados.py contém a função simular_lancamento_dados, que simula o lançamento de um dado com um número específico de faces várias vezes. Ela utiliza a biblioteca random para gerar números aleatórios entre 1 e o número de faces especificado.

```python
import random

def simular_lancamento_dados(numero_de_lancamentos, faces):
    resultados = []
    for _ in range(numero_de_lancamentos):
        resultado = random.randint(1, faces)
        resultados.append(resultado)
    return resultados
```

#### helper.py
O arquivo helper.py define a função formatar_resultados, que formata os resultados dos lançamentos de dados em uma string formatada, numerando cada lançamento.

```python
def formatar_resultados(resultados):
    formatted_result = "\n".join([f"Lançamento {i + 1}: {resultado}" for i, resultado in enumerate(resultados)])
    return formatted_result
```

Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
