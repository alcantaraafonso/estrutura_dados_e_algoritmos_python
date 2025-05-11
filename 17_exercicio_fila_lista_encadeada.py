class No:
    def __init__(self, element):
        self.element = element
        self.proximo_no = None

    def mostrar_no(self):
        print(self.element)

class ListaEncadeadaExtremidadeDupla:
    def __init__(self):
        self.__primeiro_no = None
        self.__ultimo_no = None


    def __lista_vazia(self):
        return self.__primeiro_no == None
        
    def insere_final(self, element):
        novo_no = No(element)
        if self.__lista_vazia():
            self.__primeiro_no = novo_no
        else:
            self.__ultimo_no.proximo_no = novo_no
        self.__ultimo_no = novo_no

    def mostrar_lista(self):
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
        if self.__primeiro_no.proximo_no == None:
            self.__ultimo_no = None
        
        self.__primeiro_no = self.__primeiro_no.proximo_no

    def ver_inicio(self):
        if self.__lista_vazia():
            print('Pilha vazia')
            return
        
        self.__primeiro_no.mostrar_no()

class FilaEncadeada:
    def __init__(self):
        self.lista = ListaEncadeadaExtremidadeDupla()

    def enfileirar(self, element):
        self.lista.insere_final(element)

    def desenfileirar(self):
        self.lista.excluir_inicio()
    
    def ver_inicio(self):
        self.lista.ver_inicio()

    def listar(self):
        self.lista.mostrar_lista()

fila = FilaEncadeada()

fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.enfileirar(4)
fila.listar()
fila.ver_inicio()
print('----')

fila.desenfileirar()
fila.listar()
fila.ver_inicio()