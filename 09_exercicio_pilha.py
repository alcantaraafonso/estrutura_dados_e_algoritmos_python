"""
1 - trabalhar somente com delimitadores
Chaves { e }
Colchetes [ e ]
Parênteses ( e )
2 - Cada delimitador de abertura tem um delimitador de fechamento
3 - O delimitador de fechamento deve ser o mesmo que o delimitador de abertura
exemplo:
    c[d] - correto
    a{b[c]d}e - correto
    a{b[c}d]e - errado

4 - as expressões devem ser inseridos pelo usuário via input
5 - A pilha deve empilhar apenas os delimitadores
6 - Se a pilha estiver vazia, a expressão é válida
    
"""
import numpy as np
import re

class Pilha_Validacao:
    def __init__(self, capadidade):
        self.__capacidade = capadidade
        self.__topo = -1
        self.__valores = np.chararray(self.__capacidade, unicode=True)


    def ver_topo(self):
        if self.__pilha_vazia() :
            return -1
        return self.__valores[self.__topo]
    
    def empilhar(self, element):
        if self.__pilha_cheia():
            print("Pilha cheia")
            return
        self.__topo += 1
        self.__valores[self.__topo] = element


    def desempilhar(self, element):
        if self.__pilha_vazia():
            print("Pilha vazia")
            return
        elif self.__valores[self.__topo] == element:
            self.__topo -= 1 
    
    # metodo privado
    def __pilha_cheia(self):
        return self.__topo == self.__capacidade - 1


    def pilha_vazia(self):
        return self.__topo == -1


expressao = input('Digite a expressão aritmética: ')
lista = re.findall('[(){\}\[\]]', expressao)

pilha = Pilha_Validacao(len(lista))
# print(re.findall('[(){\}\[\]]', expressao))
for i in expressao: 
    if re.search('[({\[]', i):
        pilha.empilhar(i)
        print(pilha.ver_topo())
    elif re.search('[)}\]]', i):
        element = ''
        if i == ']':
            element = '['
        elif i == '(': 
            element = ')'
        elif i == '}':
            element = '{'
        pilha.desempilhar(element)
        print(pilha.ver_topo())
     

if -1 == pilha.ver_topo():
    print("Expressão válida")
else:
    print('Expressão inválida')