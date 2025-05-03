import timeit

# O big O desta função é O(n), pois ela executa um for que está
# diretamente mente ligado ao valor de n, ou seja, o tempo de execução
# Logo, se n for 10, a função executará 11 passos
def soma1(n):
    """
    This function calculates the sum of all integers from 0 to n.
    :param n: The upper limit of the sum (inclusive).
    :return: The sum of all integers from 0 to n.
    """
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma


# Testando a função com diferentes valores de n
print("Testando a função soma1")
for n in [10, 100, 1000, 10000, 100000]:
    tempo = timeit.timeit(lambda: soma1(n), number=1000)
    print(f"Tempo para n={n}: {tempo:.6f} segundos")

# O big O desta função é O(3), pois ela executa sempre 3 operações,
# independente do valor de n, ou seja, o tempo de execução tende a ser constante
def soma2(n):
    """
    This function calculates the sum of all integers from 0 to n using the formula n*(n+1)/2.
    :param n: The upper limit of the sum (inclusive).
    :return: The sum of all integers from 0 to n.
    example: soma2(10) 
        (10 * 11) / 2 = 55

    """
    return n * (n + 1) // 2

# Testando a função com diferentes valores de n
print("Testando a função soma2")
for n in [10, 100, 1000, 10000, 100000]:
    tempo = timeit.timeit(lambda: soma2(n), number=1000)
    print(f"Tempo para n={n}: {tempo:.6f} segundos")