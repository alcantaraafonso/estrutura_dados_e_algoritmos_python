import numpy as np

class Deque:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__inicio = -1
        self.__final = 0
        self.__numero_elementos = 0
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __deque_vazio(self):
        return self.__inicio == -1
    
    def __deque_cheio(self):
        return (self.__inicio == 0 and self.__final == self.__capacidade - 1) \
            or (self.__inicio == self.__final + 1)

    def insere_inicio(self, element):
        if self.__deque_cheio():
            print('Deque cheio')
            return
        
        # se estiver vazio
        if self.__inicio == -1:
            self.__inicio = 0
            self.__final = 0

        # Inicio estiver na primeira posicao
        elif self.__inicio == 0:
            self.__inicio = self.__capacidade - 1

        else:
            self.__inicio -= 1

        self.__valores[self.__inicio] = element

    def insere_final(self, element):
        if self.__deque_cheio():
            print('Deque cheio')
            return
        
        # se estiver vazio
        if self.__inicio == -1:
            self.__inicio = 0
            self.__final = 0

        # Inicio estiver na ultima posicao
        elif self.__final == self.__capacidade - 1:
            self.__final = 0

        else:
            self.__final += 1

        self.__valores[self.__final] = element

    def excluir_inicio(self):
        if self.__deque_vazio():
            print('Deque vazio')
            return
        
        # possui somente um elemento
        if self.__inicio == self.__final:
            self.__inicio = - 1
            self.__final = -1

        else:
            # volta posição inicial
            if self.__inicio == self.__capacidade - 1:
                self.__inicio = 0
            else:
                # Incrementar inicio para remover início atual
                self.__inicio += 1

    def excluir_final(self):
        if self.__deque_vazio():
            print('Deque vazio')
            return
        
        if self.__inicio == self.__final:
            self.__inicio = -1
            self.__final = -1
        elif self.__inicio == 0:
            self.__final = self.__capacidade - 1
        else:
            self.__final -= 1
    
    def get_inicio(self):
        return -1 if self.__deque_vazio() else self.__valores[self.__inicio]
    
    def get_final(self):
        return "Deque vazio" if self.__deque_vazio() \
            or self.__final < 0 else self.__valores[self.__final]

    def inicio(self):
        return self.__inicio
    
    def final(self):
        return self.__final
    
    def imprime_fila(self):
        print(self.__valores)
        
        
deque = Deque(5)

deque.insere_final(5)
print(f'getInicio: {deque.get_inicio()} - getFinal: {deque.get_final()}')

# resultado: 5 10
deque.insere_final(10)
print(f'getInicio: {deque.get_inicio()} - getFinal: {deque.get_final()}')

# resultado: 3 5 10
deque.insere_inicio(3)
print(f'getInicio: {deque.get_inicio()} - getFinal: {deque.get_final()}')

# resultado: 2 3 5 10 11
deque.insere_inicio(2)
deque.insere_final(11)
print(f'getInicio: {deque.get_inicio()} - getFinal: {deque.get_final()}')


# resultado:  3 5 10
deque.excluir_inicio()
deque.excluir_final()
print(f'getInicio: {deque.get_inicio()} - getFinal: {deque.get_final()}')

print(f'getInicio: {deque.get_inicio()} que tá no índice {deque.inicio()} - getFinal: \
      {deque.get_final()} que tá no índice {deque.final()}')