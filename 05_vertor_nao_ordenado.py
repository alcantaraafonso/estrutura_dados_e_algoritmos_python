import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(capacidade, dtype=int)

    # O(n) 
    def imprimir(self):
        if self.ultima_posicao == -1:
            print("Vetor vazio")
        else:
            for i in range(self.ultima_posicao + 1):  # para mostrar somente posições ocupadas
                print(f"{i}: {self.valores[i]}")

    # O(1) - constante
    def inserir(self, element):
        if self.ultima_posicao == self.capacidade - 1:
            print("Vetor cheio")
            return
        self.ultima_posicao += 1
        self.valores[self.ultima_posicao] = element

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
        else:
            print("Elemento não encontrado")

vetor = VetorNaoOrdenado(5)

vetor.imprimir()

vetor.inserir(2)
vetor.imprimir()

vetor.inserir(4)
vetor.inserir(5)
vetor.inserir(8)
vetor.inserir(1)

vetor.imprimir()

vetor.inserir(7)

vetor.imprimir()
element = vetor.pesquisar(1)
if element != -1:
    print(f"Elemento encontrado na posição {element}")

vetor.imprimir()
print('Excluindo o elemento 5')
vetor.excluir(5)
print('elemento 5 exluído')
vetor.imprimir()

