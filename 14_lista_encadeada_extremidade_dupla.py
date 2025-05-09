import numpy as np

class No:
    def __init__(self, element):
        self.element = element
        self.proximo_no = None

    def mostrar_no(self):
        print(self.element)


class ListaEncadeadaExtremidadeDupla:
    def __init__(self):
        self.__cabela_lista_primeiro_no = None
        self.__cabela_lista_ultimo_no = None

    def __lista_vazia(self):
        return self.__cabela_lista_primeiro_no == None
        
    def insere_inicio(self, element):
        novo_no = No(element)
        if self.__lista_vazia():
            self.__cabela_lista_ultimo_no = novo_no
        novo_no.proximo_no = self.__cabela_lista_primeiro_no
        self.__cabela_lista_primeiro_no = novo_no

    def insere_final(self, element):
        novo_no = No(element)
        if self.__lista_vazia():
            self.__cabela_lista_primeiro_no = novo_no
        else:
            self.__cabela_lista_ultimo_no.proximo_no = novo_no
        self.__cabela_lista_ultimo_no = novo_no

    def mostrar(self):
        if self.__lista_vazia():
            print('Lista vazia')
            return 
        no_atual = self.__cabela_lista_primeiro_no
        while no_atual != None:
            no_atual.mostrar_no()
            # print(f'Cabeça primeiro_no: {self.__cabela_lista_primeiro_no} - Cabeça último nó: {self.__cabela_lista_ultimo_no}')
            no_atual = no_atual.proximo_no
        print('----')
    
    def excluir_inicio(self):
        if self.__lista_vazia():
            return
        temp = self.__cabela_lista_primeiro_no
        if temp.proximo_no == None:
            self.__cabela_lista_ultimo_no = None
        
        self.__cabela_lista_primeiro_no = self.__cabela_lista_primeiro_no.proximo_no
        return temp
    
    def pesquisa(self, element):
        if self.__lista_vazia():
            return None
        
        no_atual = self.__cabela_lista_primeiro_no
        while no_atual.element != element:
            if no_atual.proximo_no == None: 
                return None
            else:
                no_atual = no_atual.proximo_no
        return no_atual

## insere no inicio

lista = ListaEncadeadaExtremidadeDupla()
## Insere Inicio
lista.insere_inicio(1)
lista. mostrar()

lista.insere_inicio(2)
lista. mostrar()

lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista. mostrar()

## Insere Final
lista.insere_inicio(6)
lista. mostrar()

lista.insere_inicio(7)
lista. mostrar()

lista.insere_inicio(8)
lista. mostrar()

## Pesquisar -> O(n)
# pesquisa = lista.pesquisa(1)
# if pesquisa != None:
#     print('Encontrado"', pesquisa.element)
# else:
#     print('Não encontrado: ', pesquisa)

## Excluir iniicio
# lista.excluir_inicio()
# lista.mostrar()

# lista.excluir_inicio()
# lista.mostrar()
# lista.excluir_inicio()
# lista.mostrar()
# lista.excluir_inicio()
# lista.mostrar()
# lista.excluir_inicio()
# lista.mostrar()



# ## Excluir posição
# print('excluir o item #1')
# lista.excluir_posicao(1)
# lista.mostrar()

# print('excluir o item #5')
# lista.excluir_posicao(5)
# lista.mostrar()