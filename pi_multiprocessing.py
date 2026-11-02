import random
import time
import multiprocessing


def calcular_pontos(n):

    dentro = 0

    for i in range(n):

        x = random.random()
        y = random.random()

        if x*x + y*y <= 1:
            dentro += 1

    return dentro

if __name__ == "__main__":

    N = 100000000
    processos = 4

    pontos_por_processo = N // processos

    inicio = time.time()

    with multiprocessing.Pool(processos) as pool:
        resultados = pool.map(

            calcular_pontos,
            [pontos_por_processo] * processos

        )

    total_dentro = sum(resultados)

    pi = 4 * total_dentro / (pontos_por_processo * processos)
    fim = time.time()

    print(f"PI={pi}")
    print(f"Process: {processos}")
    print(f"Time: {fim - inicio:.2f} seconds")
