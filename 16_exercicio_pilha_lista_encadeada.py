class No:
    def __init__(self, element):
        self.element = element
        self.no_anterior = None

    def mostrar_no(self):
        print(self.element)

class PilhaEncadeada:
    def __init__(self):
        self.__ultimo_no = None

    def pilha_vazia(self):
        return self.__ultimo_no == None

    def empilhar(self, element):
        novo_no = No(element)
        novo_no.no_anterior = self.__ultimo_no
        self.__ultimo_no = novo_no

    def desempilhar(self):
        if self.pilha_vazia():
            return
        
        self.__ultimo_no = self.__ultimo_no.no_anterior

    def ver_topo(self):
        if self.pilha_vazia():
            print('Pilha vazia')
            return
        
        self.__ultimo_no.mostrar_no()
        
    def mostrar_pilha(self):
        if self.pilha_vazia():
            print('Pilha vazia')
            return
        atual = self.__ultimo_no
        while atual != None:
            atual.mostrar_no()
            atual = atual.no_anterior


pilha = PilhaEncadeada()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)

pilha.ver_topo()
print('---')
pilha.mostrar_pilha()

pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
pilha.ver_topo()
print('---')
pilha.mostrar_pilha()