import numpy as np

class VetorOrdenado:

    def __init__(self, capacidade):
        self.tamanho = capacidade
        self.valores = np.zeros(capacidade, dtype=int)
        self.ultima_posicao = -1

    # O(n) - linear
    def imprimir(self):
        if self.ultima_posicao == -1:
            print("Vetor vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(f"{i}: {self.valores[i]}")
            print("Vetor ordenado - fim")


    # O(n) - linear
    def inserir(self, element):
        if self.ultima_posicao == self.tamanho - 1:
            print("Vetor cheio")
            return
        pos = 0
        # primeiro, encontrar a posição correta para o novo elemento
        for i in range(self.ultima_posicao + 1):
            pos = i
            if self.valores[i] > element:
                break
            # se o elemento for maior que todos os existentes, pos será igual a ultima_posicao + 1
            if i == self.ultima_posicao:
                pos = i + 1


        # remanejar os valores/índices
        x = self.ultima_posicao
        while x >= pos:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[pos] = element
        self.ultima_posicao += 1

    # O(n) - linear
    def pesquisar(self, element):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] == element:
                return i
        return -1
    
    def excluir(self, element):
        pos = self.pesquisar(element)
        if pos != -1:
            for i in range(pos, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            
            self.ultima_posicao -= 1
    	
        return -1
        

vetor = VetorOrdenado(10)

vetor.imprimir()

vetor.inserir(6)
vetor.imprimir()

vetor.inserir(4)
vetor.imprimir()

vetor.inserir(3)
vetor.imprimir()

vetor.inserir(5)
vetor.imprimir()

vetor.inserir(1)
vetor.imprimir()

vetor.inserir(8)
vetor.imprimir()


indice = vetor.pesquisar(8)
print(f"Elemento encontrado na posição {indice}") if indice != -1 else print("Elemento não encontrado")

vetor.excluir(9)
vetor.imprimir()