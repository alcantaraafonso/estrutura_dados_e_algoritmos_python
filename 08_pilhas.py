import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.zeros(self.__capacidade, dtype=int)


    # metodo privado
    def __pilha_cheia(self):
        return self.__topo == self.__capacidade - 1


    def __pilha_vazia(self):
        return self.__topo == -1


    def empilhar(self, element):
        if self.__pilha_cheia():
            print("Pilha cheia")
            return
        self.__topo += 1
        self.__valores[self.__topo] = element


    def desempilhar(self):
        if self.__pilha_vazia():
            print("Pilha vazia")
            return
        self.__topo -= 1
        

    def ver_topo(self):
        if self.__pilha_vazia() :
            print("Pilha vazia")
            return -1
        return self.__valores[self.__topo]


pilha = Pilha(5)


print(pilha.ver_topo())
pilha.empilhar(10)
print(pilha.ver_topo())
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
print(pilha.ver_topo())
pilha.empilhar(6)

pilha.desempilhar()
print(pilha.ver_topo())

