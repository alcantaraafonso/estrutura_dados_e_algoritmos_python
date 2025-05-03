import numpy as np

class FilaPrioridade:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__numero_elementos = 0
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __fila_vazia(self):
        return self.__numero_elementos == 0
    
    def __fila_cheia(self):
        return self.__numero_elementos == self.__capacidade

    def primeiro(self):
        return -1 if self.__fila_vazia() else self.__valores[self.__numero_elementos - 1]
    
    def ultimo(self):
        return self.__valores[0] if self.__numero_elementos > 0 else "Fila Vazia"
    
    def imprime_fila(self):
        return self.__valores 

    def enfileirar(self, element):
        if self.__fila_cheia():
            print('Fila cheia')
            return
        
        if self.__numero_elementos == 0:
            self.__valores[self.__numero_elementos] = element
            self.__numero_elementos += 1
        else:
            x = self.__numero_elementos - 1
            while x >= 0: # remanejamento
                if element > self.__valores[x]:
                    self.__valores[x + 1] = self.__valores[x]
                else:
                    break
                x -= 1
            self.__valores[x + 1] = element # alocando valor após remanejamento
            self.__numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('Fila vazia')
            return
        
        valor = self.__valores[self.__numero_elementos - 1]
        self.__numero_elementos -= 1
        return valor
    

fila = FilaPrioridade(5)

print(fila.primeiro())

# tradicional: 30
# Prioridade: 30
fila.enfileirar(30)
print(fila.primeiro())

# tradicional: 50 30
# Prioridade: 50 30
fila.enfileirar(50)
print(fila.primeiro())


# tradicional: 10 50 30
# Prioridade: 50 30 10 
fila.enfileirar(10)
print(fila.primeiro())

print('Fila completa', fila.imprime_fila())

# tradicional: 40 10 50 30
# Prioridade: 50 40 30 10 
fila.enfileirar(40)
print(fila.primeiro())

# tradicional: 20 40 10 50 30
# Prioridade: 50 40 30 20 10 
fila.enfileirar(20)
print(fila.primeiro())

print('Fila completa', fila.imprime_fila())
print(f'primeiro valor = {fila.primeiro()} ')
print(f'ultimo valor = {fila.ultimo()}')

fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
print('Fila completa', fila.imprime_fila())
print(f'primeiro valor = {fila.primeiro()} ')
print(f'ultimo valor = {fila.ultimo()}')