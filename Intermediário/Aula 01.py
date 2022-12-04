"""
----------------------------Introdução às funções (def) em Python-------------------------------

# Funções são trechos de código usados para
  replicar determinada ação ao longo do código

# Elas podem receber valores para parâmetros (argumentos)
  e retornar um valor específico

# Por padrão, funções Python retornam None (nada)

"""

def Print():
    print("Hello world!")


def imprimir(a, b, c):  # Parâmetros
    print(a, b, c)

def saudacao(nome='Sem nome'):  #Caso não envie nenhum argumento para o parâmetro nome
    print(f'Olá {nome}')

Print()
imprimir(1, 2, 3)  # Argumentos
saudacao("Matheus Carvalho")
saudacao()
