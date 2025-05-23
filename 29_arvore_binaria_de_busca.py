class No:
    def __init__(self, element):
        self.element = element
        self.no_da_esquerda = None
        self.no_da_direita = None

    def mostrar_no(self):
        print(self.element)


class ArvoreBinariaBusca:
    def __init__(self):
        self._raiz = None

    def arvore_vazia(self):
        return self._raiz == None

    def inserir_no(self, element):
        novo_no = No(element)
        if self.arvore_vazia():
            self._raiz = novo_no
            return
        
        # só primeiro nível
        # fazer um while com um if?
        no_atual = self._raiz
        while True:
            no_pai = no_atual
            if element < no_atual.element:
                no_atual= no_atual.no_da_esquerda
                if no_atual == None:
                    no_pai.no_da_esquerda = novo_no
                    return
            else:
                no_atual = no_atual.no_da_direita
                if no_atual == None:
                    no_pai.no_da_direita = novo_no
                    return

    def inserir(self, valor):
        if self._raiz is None:
            # Caso base: árvore vazia
            self._raiz = No(valor)
        else:
            # Chama o método auxiliar recursivo
            self._inserir_recursivo(valor, self._raiz, None)
    
    def _inserir_recursivo(self, valor, no_atual, no_pai):
        # Caso base: encontrou a posição para inserir
        if no_atual is None:
            novo_no = No(valor)
            # Decide se insere à esquerda ou à direita do pai
            if valor < no_pai.valor:
                no_pai.esquerda = novo_no
            else:
                no_pai.direita = novo_no
        
            # Registra a ligação
            # self.ligacoes.append(str(no_pai.valor) + '->' + str(novo_no.valor))
            return
        
        # Casos recursivos
        if valor < no_atual.valor:
            # Continua a busca à esquerda
            self._inserir_recursivo(valor, no_atual.esquerda, no_atual)
        else:
            # Continua a busca à direita
            self._inserir_recursivo(valor, no_atual.direita, no_atual)

    def pesquisar_valor(self, element):
        if self.arvore_vazia():
            print('A árvore está vazia')
            return
        else:
            no_atual = self._raiz
            #  while no_atual .element != element:
            while no_atual.element != element:
                if element < no_atual.element:
                    no_atual = no_atual.no_da_esquerda
                else:
                    no_atual = no_atual.no_da_direita           
                if no_atual == None:
                    return None
            return no_atual
                

    # def __pesquisar_element_recursivo(self, element, no_atual: No):
    #      # condição de parada
    #     if no_atual is None:
    #         return None
        
    #     # Casos recursivos
    #     if element < no_atual.element:
    #         # Continua a busca à esquerda
    #         self.__pesquisar_element_recursivo(element, no_atual.no_da_esquerda)
    #         print(no_atual)
    #         if element == no_atual.element:
    #             return no_atual
    #         else:
    #             return None
    #     else:
    #         # Continua a busca à direita
    #         self.__pesquisar_element_recursivo(element, no_atual.no_da_direita)
    #         print(no_atual)
    #         if element == no_atual.element:
    #             return no_atual
    #         else:
    #             return None
        
    def mostrar_arvore(self) :
        if self.arvore_vazia() == None: 
            return
        
        self.__mostrar_arvore_recursiva(self._raiz)
        print('-----------')

    def __mostrar_arvore_recursiva(self, no, level = 0):
        if no == None:
            return
        self.__mostrar_arvore_recursiva(no.no_da_direita, level+1)
        print ('  '*level + str(no.element))
        self.__mostrar_arvore_recursiva(no.no_da_esquerda, level+1)

    # Raiz, esquerda, direita
    def travessia_pre_ordem(self, no_atual: No):
        # condição de parada
        if no_atual != None:
            print(no_atual.element)
            self.travessia_pre_ordem(no_atual.no_da_esquerda)
            self.travessia_pre_ordem(no_atual.no_da_direita)
    
    # Esquerda, raiz, direita
    # Ideal para ordenar a árvore de forma crescente
    def travessia_ordem(self, no_atual: No):
        # condição de parada
        if no_atual != None:
            self.travessia_ordem(no_atual.no_da_esquerda)
            print(no_atual.element)
            self.travessia_ordem(no_atual.no_da_direita)

    # Esquerda, Direita, Raiz
    def travessia_pos_ordem(self, no_atual: No):
        # condição de parada
        if no_atual != None:
            self.travessia_pos_ordem(no_atual.no_da_esquerda)
            self.travessia_pos_ordem(no_atual.no_da_direita)
            print(no_atual.element)

    # def excluir_no(self, element):
    #     if self.arvore_vazia():
    #         print('Árvore vazia')
    #         return
    #     no_atual = no_pai = self._raiz
    #     is_esquerda = True
    #     while element != no_atual.element:
    #         no_pai = no_atual
    #         if element < no_atual.element:
    #             is_esquerda = True
    #             no_atual = no_atual.no_da_esquerda
    #         else:
    #             is_esquerda = False
    #             no_atual = no_atual.no_da_direita
    #         if no_atual == None:
    #             return False
            
    #     # Nó atual é uma folha
    #     if no_atual.no_da_esquerda == None and no_atual.no_da_direita == None:
    #         if no_atual == self._raiz:
    #             self._raiz = None
    #         elif is_esquerda:
    #             no_pai.no_da_esquerda = None
    #         else:
    #             no_pai.no_da_direita = None

    #     # o nó a ser apagado não possui filho na direita
    #     elif no_atual.no_da_direita == None:
    #         if no_atual == self._raiz:
    #             self._raiz = no_atual.no_da_esquerda
    #         elif is_esquerda:
    #             no_pai.no_da_esquerda = no_atual.no_da_esquerda
    #         else:
    #             no_pai.no_da_direita = no_atual.no_da_esquerda
    #     # o nó a ser apagado não possui filho na esquerda 
    #     elif no_atual.no_da_esquerda == None:
    #         if no_atual == self._raiz:
    #             self._raiz = no_atual.no_da_direita
    #         elif is_esquerda:
    #             no_pai.no_da_esquerda = no_atual.no_da_direita
    #         else:
    #             no_pai.no_da_direita = no_atual.no_da_direita

    #     # o nó a ser apagado tem dois filhos
    #     else:
    #         sucessor = self.get_sucessor(no_atual)
    #         if no_atual == self._raiz:
    #             self._raiz = sucessor
    #         elif is_esquerda:
    #             no_pai.no_da_esquerda = sucessor
    #         else:
    #             no_pai.no_da_direita = sucessor
    #         sucessor.no_da_esquerda = no_atual.no_da_esquerda

    #     return True


    def get_sucessor(self, no: No):
        pai_sucessor = no
        sucessor = no
        no_atual = no.no_da_direita

        while no_atual != None:
            pai_sucessor = sucessor
            sucessor = no_atual
            no_atual = no_atual.no_da_esquerda

        if sucessor != no.no_da_direita:
            pai_sucessor.no_da_esquerda = sucessor.no_da_direita
            sucessor.no_da_direita = no
        return sucessor


    def excluir_no(self, valor):
        def remover_no(no, valor):
            if no is None:
                return no
            if valor < no.element:
                no.no_da_esquerda = remover_no(no.no_da_esquerda, valor)
            elif valor > no.element:
                no.no_da_direita = remover_no(no.no_da_direita, valor)
            else:
                # Caso 1: Nó folha
                if no.no_da_esquerda is None and no.no_da_direita is None:
                    return None
                # Caso 2: Um filho
                elif no.no_da_esquerda is None:
                    return no.no_da_direita
                elif no.no_da_direita is None:
                    return no.no_da_esquerda
                # Caso 3: Dois filhos
                else:
                    sucessor = self.get_sucessor(no)
                    no.element = sucessor.element
                    no.no_da_direita = remover_no(no.no_da_direita, sucessor.element)
            return no
    
        self._raiz = remover_no(self._raiz, valor)

arvore = ArvoreBinariaBusca()


arvore.inserir_no(53)
arvore.inserir_no(30)
arvore.inserir_no(14)
arvore.inserir_no(39)
arvore.inserir_no(9)
arvore.inserir_no(23)
arvore.inserir_no(34)
arvore.inserir_no(49)
arvore.inserir_no(72)
arvore.inserir_no(61)
arvore.inserir_no(84)
arvore.inserir_no(79)

if arvore.pesquisar_valor(9) == None:
    print('Não encontrado')
else:
    print('Encontrado')

# print('Travessia pré-ordem')
# arvore.travessia_pre_ordem(arvore._raiz)
# print('Fim - Travessia pré-ordem')

# print('Travessia ordem')
# arvore.travessia_ordem(arvore._raiz)
# print('Fim - Travessia ordem')

# print('Travessia pós ordem')
# arvore.travessia_pos_ordem(arvore._raiz)
# print('Fim - Travessia pós ordem')

# arvore.excluir_no(9)
# arvore.mostrar_arvore()

# arvore.excluir_no(79)
# arvore.mostrar_arvore()

# arvore.mostrar_arvore()
# arvore.excluir_no(84)
# arvore.mostrar_arvore()

# arvore.mostrar_arvore()
# arvore.excluir_no(9)
# arvore.mostrar_arvore()

# arvore.mostrar_arvore()
# arvore.excluir_no(14)
# arvore.mostrar_arvore()


arvore.mostrar_arvore()
arvore.excluir_no(72)
arvore.mostrar_arvore()
arvore.excluir_no(30)
arvore.mostrar_arvore()