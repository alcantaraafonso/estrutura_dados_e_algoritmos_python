import numpy as np

class No:
    def __init__(self, element):
        self.element = element
        self.proximo_no = None
        self.no_anterior = None

    def mostrar_no(self):
        print(self.element)


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.__cabela_lista_primeiro_no = None
        self.__cabela_lista_ultimo_no = None

    def __lista_vazia(self):
        return self.__cabela_lista_primeiro_no == None 
        
    def insere_inicio(self, element):
        novo_no = No(element)
        if self.__lista_vazia():
            self.__cabela_lista_ultimo_no = novo_no
        else:
            self.__cabela_lista_primeiro_no.no_anterior = novo_no
        novo_no.proximo_no = self.__cabela_lista_primeiro_no
        self.__cabela_lista_primeiro_no = novo_no

    def insere_final(self, element):
        novo_no = No(element)
        if self.__lista_vazia():
            self.__cabela_lista_primeiro_no = novo_no
        else:
            self.__cabela_lista_ultimo_no.proximo_no = novo_no
        self.__cabela_lista_ultimo_no = novo_no

    def mostrar_do_inicio(self):
        if self.__lista_vazia():
            print('Lista vazia')
            return 
        no_atual = self.__cabela_lista_primeiro_no
        while no_atual != None:
            no_atual.mostrar_no()
            # print(f'Cabeça primeiro_no: {self.__cabela_lista_primeiro_no} - Cabeça último nó: {self.__cabela_lista_ultimo_no}')
            no_atual = no_atual.proximo_no
        print('----')
    
    def mostrar_do_final(self):
        if self.__lista_vazia():
            print('Lista vazia')
            return 
        no_atual = self.__cabela_lista_ultimo_no
        while no_atual != None:
            no_atual.mostrar_no()
            # print(f'Cabeça primeiro_no: {self.__cabela_lista_primeiro_no} - Cabeça último nó: {self.__cabela_lista_ultimo_no}')
            no_atual = no_atual.no_anterior
        print('----')
    
    def excluir_inicio(self):
        temp = self.__cabela_lista_primeiro_no
        if self.__lista_vazia():
            return
        if self.__cabela_lista_primeiro_no.proximo_no == None:
            self.__cabela_lista_ultimo_no = None
        else:
            self.__cabela_lista_primeiro_no.proximo_no.no_anterior = None
        self.__cabela_lista_primeiro_no = self.__cabela_lista_primeiro_no.proximo_no

    def excluir_final(self):
        temp = self.__cabela_lista_ultimo_no
        if self.__lista_vazia():
            return
        if self.__cabela_lista_primeiro_no.proximo_no == None:
            self.__cabela_lista_primeiro_no = None
        else:
            self.__cabela_lista_ultimo_no.no_anterior.proximo_no = None
        self.__cabela_lista_ultimo_no = self.__cabela_lista_ultimo_no.no_anterior
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

lista = ListaDuplamenteEncadeada()
## Insere Inicio
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista. mostrar_do_inicio()
lista. mostrar_do_final()

## Insere Final
# lista.insere_final(6)
# lista.insere_final(7)
# lista.insere_final(8)
# lista. mostrar_do_inicio()
# lista. mostrar_do_final()

## Pesquisar -> O(n)
# pesquisa = lista.pesquisa(1)
# if pesquisa != None:
#     print('Encontrado"', pesquisa.element)
# else:
#     print('Não encontrado: ', pesquisa)

## Excluir iniicio
lista.excluir_inicio()
lista.mostrar_do_inicio()

## Excluir final
lista.excluir_final()
lista.mostrar_do_inicio()

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