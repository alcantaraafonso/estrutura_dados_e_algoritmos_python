import numpy as np

class FilaCircular:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__inicio = 0
        self.__final = -1
        self.__numero_elementos = 0
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __fila_vazia(self):
        return self.__numero_elementos == 0
    
    def __fila_cheia(self):
        return self.__numero_elementos == self.__capacidade
    
    def enfileirar(self, element):
        if self.__fila_cheia():
            print('Fila cheia')
            return
        # só entra aqui qdo a fila está cheia e assim faz o remanejamento
        if self.__final == self.__capacidade - 1:
            self.__final = -1

        self.__final += 1
        self.__valores[self.__final] = element
        self.__numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('Fila vazia')
            return
        
        temp = self.__valores[self.__inicio]
        self.__inicio += 1

        if self.__inicio == self.__capacidade:
            self.__inicio = 0
        self.__numero_elementos -= 1
        return temp
    
    def primeiro(self):
        return -1 if self.__fila_vazia() else self.__valores[self.__inicio]
    
    def ultimo(self):
        return self.__valores[self.__final] if self.__fila_cheia() else -1

    def inicio(self):
        return self.__inicio
    
    def final(self):
        return self.__final
    
    def imprime_fila(self):
        print(self.__valores)
    

fila = FilaCircular(5)

print(fila.primeiro())

# 1
fila.enfileirar(1)
print(fila.primeiro())

# 2 1
fila.enfileirar(2)
print(fila.primeiro())

# 5 4 3 2 1
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
print(fila.primeiro())

fila.enfileirar(6)

print('Desenfileirar')
# 5 4 3
fila.desenfileirar()
fila.desenfileirar()
print(fila.primeiro())

# 7 6 5 4 3
print('Enfileirar')
fila.enfileirar(6)
fila.enfileirar(7)
print(fila.primeiro())


print('Fila completa', fila.imprime_fila())
print(f'primeiro valor = {fila.primeiro()} no índice: {fila.inicio()} ')
print(f'ultimo valor = {fila.ultimo()} no índice: {fila.final()} ')



