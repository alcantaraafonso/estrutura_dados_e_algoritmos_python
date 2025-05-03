# exemplos de Big O


# O(1) - Tempo constante
lista = [1, 2, 3, 4, 5]

def constant(n):
    return n[0]

print('O(1) - Tempo constante')
print(constant(lista))

# O(n) - Tempo linear
def linear(n):
    for i in n:
        print(i)

print('O(n) - Tempo linear')
linear(lista)

# O(n^2) - Tempo quadrático - polynomial
def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)
        print('---')

print('O(n^2) - Tempo quadrático')
quadratic(lista)

# Combination
# O(1) + O(5) + O(n) + O(n) + O(3)
# O(9) + O(2n) -> O(n)
# Como o resultado foi O(n), o algorítmo 
# pode ser categorizado como quadrático ou cúbico ou exponencial
def combination(n):
    # O(1) - Tempo constante
    print(n[0])

    # O(5) - Tempo constante
    for i in range(5):
        print('test', i)

    # O(n) - Tempo linear
    for i in n:
        print(i)

    #O(n) - Tempo linear
    for i in n:
        print(i)

    # O(3) - Tempo constante
    print('Python')
    print('Python')
    print('Python')

combination(lista)