import numpy as np
class VetorOrdenado:

  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    # Mudança no tipo de dados
    self.valores = np.empty(self.capacidade, dtype=object)

  # Referência para o vértice e comparação com a distância para o objetivo
  def insere(self, vertice):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return
    posicao = 0
    for i in range(self.ultima_posicao + 1):
      posicao = i
      if self.valores[i].distancia_objetivo > vertice.distancia_objetivo:
        break
      if i == self.ultima_posicao:
        posicao = i + 1
    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      x -= 1
    self.valores[posicao] = vertice
    self.ultima_posicao += 1

  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i].rotulo, ' - ', self.valores[i].distancia_objetivo)

class Vertice:
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.distancia_objetivo = distancia_objetivo
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
    arad = Vertice('Arad', 366)
    zerind = Vertice('Zerind', 374)
    oradea = Vertice('Oradea', 380)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    dobreta = Vertice('Dobreta', 242)
    craiova = Vertice('Craiova', 160)
    rimnicu = Vertice('Rimnicu', 193)
    fagaras = Vertice('Fagaras', 178)
    pitesti = Vertice('Pitesti', 98)
    bucharest = Vertice('Bucharest', 0)
    giurgiu = Vertice('Giurgiu', 77)

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

class BuscaGulosa:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False

  def buscar(self, atual):
    print('-------')
    print('Atual: {}'.format(atual.rotulo))
    atual.visitado = True

    if atual == self.objetivo:
        self.encontrado = True
        return
    else:
        # Cria um vetor ordenado para cada vértice atual
        vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
        for adjacente in atual.adjacentes:
            if adjacente.vertice.visitado == False:
                adjacente.vertice.visitado == True
                vetor_ordenado.insere(adjacente.vertice)
        vetor_ordenado.imprime()

        if vetor_ordenado.valores[0] != None:
            # passa-se o índice pois trta-se de um vetor ordenado em ordem crescente de distância
            self.buscar(vetor_ordenado.valores[0])

grafo = Grafo()
busca_gulosa = BuscaGulosa(grafo.bucharest) #destino
busca_gulosa.buscar(grafo.arad) #origem