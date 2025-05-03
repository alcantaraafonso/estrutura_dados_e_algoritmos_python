import numpy as np

class No:
    def __init__(self, element):
        self.element = element
        self.proximo_no = None

    def mostrar_no(self):
        print(self.element)


class ListaEncadeada:
    def __init__(self):
        self.__primeiro_no = None

    def __lista_vazia(self):
        return self.__primeiro_no == None
        
    def insere_inicio(self, element):
        novo_no = No(element)
        novo_no.proximo_no = self.__primeiro_no
        self.__primeiro_no = novo_no

    def mostrar(self):
        if self.__lista_vazia():
            print('Lista vazia')
            return 
        atual = self.__primeiro_no
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo_no
        print('----')
    
    def excluir_inicio(self):
        if self.__lista_vazia():
            return
        # temp = self.__primeiro
        self.__primeiro_no = self.__primeiro_no.proximo_no
        return self.__primeiro_no
    
    def pesquisa(self, element):
        if self.__lista_vazia():
            return None
        
        no_atual = self.__primeiro_no
        while no_atual.element != element:
            if no_atual.proximo_no == None: 
                return None
            else:
                no_atual = no_atual.proximo_no
        return no_atual

    def excluir_posicao(self, element):
        if self.__lista_vazia():
            return
        no_atual = self.__primeiro_no
        no_anterior = self.__primeiro_no
        while no_atual.element != element:
            if no_atual.proximo_no == None: 
                return None
            else:
                no_anterior = no_atual
                no_atual = no_atual.proximo_no

        if no_atual == self.__primeiro_no:
            self.__primeiro_no = self.excluir_inicio()
        else:
            no_anterior.proximo_no = no_atual.proximo_no

        return no_atual
## insere no inicio

lista = ListaEncadeada()
lista.insere_inicio(1)
lista. mostrar()

lista.insere_inicio(2)
lista. mostrar()

lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista. mostrar()


pesquisa = lista.pesquisa(1)
if pesquisa != None:
    print('Encontrado"', pesquisa.element)
else:
    print('Não encontrado: ', pesquisa)

## Excluir iniicio
lista.excluir_inicio()
lista.mostrar()

lista.excluir_inicio()
lista.mostrar()
lista.excluir_inicio()
lista.mostrar()
lista.excluir_inicio()
lista.mostrar()
lista.excluir_inicio()
lista.mostrar()



## Excluir posição
print('excluir o item #1')
lista.excluir_posicao(1)
lista.mostrar()

print('excluir o item #5')
lista.excluir_posicao(5)
lista.mostrar()