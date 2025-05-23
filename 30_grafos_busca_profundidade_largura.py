import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.zeros(self.__capacidade, dtype=object)


    # metodo privado
    def __pilha_cheia(self):
        return self.__topo == self.__capacidade - 1


    def __pilha_vazia(self):
        return self.__topo == -1


    def empilhar(self, element):
        if self.__pilha_cheia():
            print("Pilha cheia")
            return
        self.__topo += 1
        self.__valores[self.__topo] = element


    def desempilhar(self):
        if self.__pilha_vazia():
            print("Pilha vazia")
            return
        else:
            temp = self.__valores[self.__topo]
            self.__topo -= 1
            return temp

    def ver_topo(self):
        if self.__pilha_vazia() :
            print("Pilha vazia")
            return -1
        return self.__valores[self.__topo]

class FilaCircular:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__inicio = 0
        self.__final = -1
        self.__numero_elementos = 0
        self.__valores = np.empty(self.__capacidade, dtype=object)

    def __fila_vazia(self):
        return self.__numero_elementos == 0
    
    def __fila_cheia(self):
        return self.__numero_elementos == self.__capacidade
    
    def enfileirar(self, element):
        if self.__fila_cheia():
            print('Fila cheia')
            return
        # só entra aqui qdo a fila está cheia e assim faz o remanejamento
        if self.__final == self.__capacidade - 1:
            self.__final = -1

        self.__final += 1
        self.__valores[self.__final] = element
        self.__numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('Fila vazia')
            return
        
        temp = self.__valores[self.__inicio]
        self.__inicio += 1

        if self.__inicio == self.__capacidade:
            self.__inicio = 0
        self.__numero_elementos -= 1
        return temp
    
    def primeiro(self):
        return -1 if self.__fila_vazia() else self.__valores[self.__inicio]

    def get_tamanho_fila(self):
        return -1 if self.__fila_vazia() else self.__numero_elementos
    
    def ultimo(self):
        return self.__valores[self.__final] if self.__fila_cheia() else -1

    def inicio(self):
        return self.__inicio
    
    def final(self):
        return self.__final
    
    def imprime_fila(self):
        print(self.__valores)

class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo
        self.visitado = False # Dizer se um vértice já foi visitado
        self.adjacentes = []


    def adicionar_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostrar_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)


class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
    

class Grafo:
    arad = Vertice('Arad')
    zerind = Vertice('Zerind')
    oradea = Vertice('Oradea')
    sibiu = Vertice('Sibiu')
    timisoara = Vertice('Timisoara')
    lugoj = Vertice('Lugoj')
    mehadia = Vertice('Mehadia')
    dobreta = Vertice('Dobreta')
    craiova = Vertice('Craiova')
    rimnicu = Vertice('Rimnicu')
    fagaras = Vertice('Fagaras')
    pitesti = Vertice('Pitesti')
    bucharest = Vertice('Bucharest')
    giurgiu = Vertice('Giurgiu')

    arad.adicionar_adjacente(Adjacente(zerind, 75))
    arad.adicionar_adjacente(Adjacente(sibiu, 140))
    arad.adicionar_adjacente(Adjacente(timisoara, 118))

    zerind.adicionar_adjacente(Adjacente(arad, 75))
    zerind.adicionar_adjacente(Adjacente(oradea, 71))

    oradea.adicionar_adjacente(Adjacente(zerind, 71))
    oradea.adicionar_adjacente(Adjacente(sibiu, 151))

    sibiu.adicionar_adjacente(Adjacente(oradea, 151))
    sibiu.adicionar_adjacente(Adjacente(arad, 140))
    sibiu.adicionar_adjacente(Adjacente(fagaras, 99))
    sibiu.adicionar_adjacente(Adjacente(rimnicu, 80))

    timisoara.adicionar_adjacente(Adjacente(arad, 118))
    timisoara.adicionar_adjacente(Adjacente(lugoj, 111))

    lugoj.adicionar_adjacente(Adjacente(timisoara, 111))
    lugoj.adicionar_adjacente(Adjacente(mehadia, 70))

    mehadia.adicionar_adjacente(Adjacente(lugoj, 70))
    mehadia.adicionar_adjacente(Adjacente(dobreta, 75))

    dobreta.adicionar_adjacente(Adjacente(mehadia, 75))
    dobreta.adicionar_adjacente(Adjacente(craiova, 120))

    craiova.adicionar_adjacente(Adjacente(dobreta, 120))
    craiova.adicionar_adjacente(Adjacente(pitesti, 138))
    craiova.adicionar_adjacente(Adjacente(rimnicu, 146))

    rimnicu.adicionar_adjacente(Adjacente(craiova, 146))
    rimnicu.adicionar_adjacente(Adjacente(sibiu, 80))
    rimnicu.adicionar_adjacente(Adjacente(pitesti, 97))

    fagaras.adicionar_adjacente(Adjacente(sibiu, 99))
    fagaras.adicionar_adjacente(Adjacente(bucharest, 211))

    pitesti.adicionar_adjacente(Adjacente(rimnicu, 97))
    pitesti.adicionar_adjacente(Adjacente(craiova, 138))
    pitesti.adicionar_adjacente(Adjacente(bucharest, 101))

    bucharest.adicionar_adjacente(Adjacente(fagaras, 211))
    bucharest.adicionar_adjacente(Adjacente(pitesti, 101))
    bucharest.adicionar_adjacente(Adjacente(giurgiu, 90))


class BuscaProfundidade():
    def __init__(self, vertice):
        self.vertice = vertice
        self.vertice.visitado = True
        self.pilha = Pilha(20)
        self.pilha.empilhar(vertice)


    def buscar(self):
        topo_pilha = self.pilha.ver_topo()
        print('Topo: {}'.format(topo_pilha.rotulo))

        # For para percorrer os adjacentes do elemento que está no topo da pilha
        for adjacente in topo_pilha.adjacentes:
            print('Topo é {}. {} já foi visitada? {}' \
                .format(topo_pilha.rotulo, adjacente.vertice.rotulo, adjacente.vertice.visitado))
            if adjacente.vertice.visitado == False:
                adjacente.vertice.visitado = True
                self.pilha.empilhar(adjacente.vertice)
                print('Empilhou {}'.format(adjacente.vertice.rotulo))
                self.buscar()
        print('Desempilhou: {}'.format(self.pilha.desempilhar().rotulo))
        print()


class BuscaLargura():
    def __init__(self, vertice_inicio: Vertice):
        self.vertice_inicio = vertice_inicio
        self.vertice_inicio.visitado = True
        self.fila = FilaCircular(20)
        self.fila.enfileirar(vertice_inicio)

        
    def buscar(self):
        primeiro_vertice = self.fila.primeiro()
        print('-----')
        print('Primeiro da fila: {}'.format(primeiro_vertice.rotulo))
        
        # Desenfileira o vértice que iniciou a busca
        temp = self.fila.desenfileirar()

        print('Desenfileirou {}'.format(temp.rotulo))
        for adjacente in primeiro_vertice.adjacentes:
            print('Primeiro era {}. {} já foi visitado? {}' \
                  .format(temp.rotulo, adjacente.vertice.rotulo, adjacente.vertice.visitado))
            if adjacente.vertice.visitado == False:
                adjacente.vertice.visitado = True
                self.fila.enfileirar(adjacente.vertice)
                print('Enfileirou: {}'.format(adjacente.vertice.rotulo))
        # na busca em largura, primeiro se enfileira todos os vértices para depois fazer a chamada recursiva
        if self.fila.get_tamanho_fila() > 0:
            self.buscar()


grafo = Grafo()
busca_profundidade = BuscaProfundidade(grafo.arad)
# busca_profundidade.buscar()

print('---------')
busca_largura = BuscaLargura(grafo.arad)
busca_largura.buscar()