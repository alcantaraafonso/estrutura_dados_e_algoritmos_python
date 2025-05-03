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

    # O(log n)
    def pesquisar_binaria(self, element):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        # while limite_inferior <= limite_superior:
        #     posicao_atual = (limite_inferior + limite_superior) // 2 # Divisão inteira - int
        #     if self.valores[posicao_atual] == element:
        #         return posicao_atual
        #     elif limite_inferior > limite_superior:
        #         return -1
        #     elif self.valores[posicao_atual] < element:
        #         limite_inferior = posicao_atual + 1
        #     else:
        #         limite_superior = posicao_atual - 1
        while True:
            posicao_atual = (limite_inferior + limite_superior) // 2

            #se o elemento for encontrado na primeira tentativa
            if self.valores[posicao_atual] == element:
                return posicao_atual
            #se o elemento não for encontrado
            elif limite_inferior > limite_superior:
                return -1
            # divide os limites
            else:
                # limite_inferior
                if self.valores[posicao_atual] < element:
                    limite_inferior = posicao_atual + 1
                # limite_superior
                else:
                    limite_superior = posicao_atual - 1

    
    def excluir(self, element):
        pos = self.pesquisar_binaria(element)
        if pos != -1:
            for i in range(pos, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            
            self.ultima_posicao -= 1
    	
        return -1
        

vetor = VetorOrdenado(10)

vetor.imprimir()
vetor.inserir(8)
vetor.inserir(9)
vetor.inserir(4)
vetor.inserir(1)
vetor.inserir(5)
vetor.inserir(7)
vetor.inserir(11)
vetor.inserir(13)
vetor.inserir(2)

vetor.imprimir()


indice = vetor.pesquisar_binaria(7)
print(f"Elemento encontrado na posição {indice}") if indice != -1 else print("Elemento não encontrado")

indice = vetor.pesquisar_binaria(5)
print(f"Elemento encontrado na posição {indice}") if indice != -1 else print("Elemento não encontrado")

indice = vetor.pesquisar_binaria(13)
print(f"Elemento encontrado na posição {indice}") if indice != -1 else print("Elemento não encontrado")

indice = vetor.pesquisar_binaria(20)
print(f"Elemento encontrado na posição {indice}") if indice != -1 else print("Elemento não encontrado")
