import math
import sys
import numpy as np
import time

sys.setrecursionlimit(10000)

#Exercício 1
#Para ser primo ele deve ser divisível por 1 e ele mesmo.
#Ou seja, não pode ser divisível por nenhum número entre 2 e a raiz quadrada de n (já que após a raiz quadrada, os divisores se repetem).

def primo_iterativo(n):

    #1 e números negativos não são primos
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    raiz_n = int(math.sqrt(n))

    for i in range(2, raiz_n + 1):
        if n % i == 0:
            return False
        
    return True

def primo_recursivo(n, divisor=2):

    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    raiz_n = int(math.sqrt(n))

    if divisor > raiz_n:
        return True
    
    if n % divisor == 0:
        return False
    
    return primo_recursivo(n, divisor + 1)

def achar_maior_primo(vetor, funcao=primo_iterativo):

    maior_primo = -1

    for i in range(len(vetor)):
        if vetor[i] > maior_primo and funcao(vetor[i]):
            maior_primo = vetor[i]

    if maior_primo == -1:
        return None
    return maior_primo

if __name__ == "__main__":

    media_tempo_iterativo = 0
    media_tempo_recursivo = 0

    iteracoes = 1000

    for _ in range(iteracoes):
        vetor = np.random.randint(1, 10000000, size=100000)

        tempo_inicio_iterativo = time.time()
        maior_primo_iterativo = achar_maior_primo(vetor, primo_iterativo)
        tempo_fim_iterativo = time.time()

        tempo_inicio_recursivo = time.time()
        maior_primo_recursivo = achar_maior_primo(vetor, primo_recursivo)
        tempo_fim_recursivo = time.time()

        print(f"---------------------------------------------------------------")
        print(f"Maior número primo (iterativo): {maior_primo_iterativo}")
        print(f"Tempo gasto (iterativo): {tempo_fim_iterativo - tempo_inicio_iterativo:.4f} segundos")
        print(f"---------------------------------------------------------------")
        print(f"Maior número primo (recursivo): {maior_primo_recursivo}")
        print(f"Tempo gasto (recursivo): {tempo_fim_recursivo - tempo_inicio_recursivo:.4f} segundos")
        print(f"---------------------------------------------------------------")

        media_tempo_iterativo += (tempo_fim_iterativo - tempo_inicio_iterativo)
        media_tempo_recursivo += (tempo_fim_recursivo - tempo_inicio_recursivo)

    print(f"Resultados médios após {iteracoes} iterações:")
    print(f"Tempo médio gasto (iterativo): {media_tempo_iterativo / iteracoes:.4f} segundos, com duração total de {media_tempo_iterativo:.4f} segundos")
    print(f"Tempo médio gasto (recursivo): {media_tempo_recursivo / iteracoes:.4f} segundos, com duração total de {media_tempo_recursivo:.4f} segundos")