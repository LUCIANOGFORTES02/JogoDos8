import copy
import numpy 
from random import shuffle
from time import sleep
from heapq import heappush, heappop


#resposta=[['1','2','3'],['8','0','4'],['7','6','5']]
#matriz=[ ['0','1','2'],['7','8','3'],['6','5','4'] ]
#Resultado esperado
resposta=[['1','2','3'],['4','5','6'],['7','8','0']]

#matriz=[['1','3','6'],['4','2','0'],['7','5','8']]
matriz=[['1','3','0'],['4','5','6'],['7','8','2']]
#matriz=[['4','1','3'],['5','6','0'],['7','8','2']]
#matriz=[['0','6','1'],['4','5','3'],['7','8','2']]
#matriz=[['6','5','1'],['4','8','0'],['7','2','3']]



#matriz=[ ['1','2','3'],['4','5','0'],['6','7','8'] ]
#matriz=[ ['1','3','0'],['4','5','6'],['7','8','2'] ]
#matriz=[ ['1','2','3'],['7','4','5'],['0','8','6'] ]

 
#nao encontra solução
#matriz=[ ['2','3','1'],['4','5','7'],['6','8','0'] ] #ñ é encontrada na busca gulosa
#matriz=[ ['7','8','0'],['4','5','6'],['2','1','3'] ] #não é encontrada na busca gulosa nem na heuristica
#matriz=[ ['8','7','6'],['5','4','3'],['2','1','0'] ] #não é encontrada na busca gulosa nem na heuristica
#matriz=[ ['2','3','1'],['4','5','7'],['6','8','0'] ] #não é encontrada na busca gulosa 

#Criar tabuleiro
def imprimindoTablueiro(matriz):
    for i in range(0,3):
        print("|".join(matriz[i]))#unir as strings

        if(i<2):
            print("------")
    print("\n")

def criandoTabuleiro():
    print ("Digite o estado inicial :")
    matriz=[]
    for i in range(0,3):
        linha=[]
        for j in range (0,3):
            linha.append(str(input("Digite o valor [" + str(i) + "," + str(j) + "]:")))
            #linha.append('0')
        matriz.append(linha)
    return matriz
        

 
#Função para verificar se o movimento é valido
def verifica(x,y):
    v = True
    if (x < 0 or x > 2):
        v = False
    if (y < 0 or y > 2): 
        v = False

    return v

#Função para realizar os movimentos
#Recebe como parametros a matriz
#Gera todos os filhos do estado em branco 
def movimento(matriz):
    jogadas=[]#Gravar as jogadas
    valor='0'
    x,y=localizar(matriz,valor)
   
    #sobe
    Vx=x-1
    Vy=y
    if verifica(Vx,Vy):#realiza as trocas dos elementos
        copia= copy.deepcopy(matriz)
        m=copia[x][y]
        copia[x][y]=copia[Vx][Vy]
        copia[Vx][Vy]=m
        jogadas.append(copia)

    #desce
    Vx=x+1
    Vy=y
    if verifica(Vx,Vy):
        copia= copy.deepcopy(matriz)
        m=copia[x][y]
        copia[x][y]=copia[Vx][Vy]
        copia[Vx][Vy]=m
        jogadas.append(copia)

    #direita
    Vx=x
    Vy=y+1
    if verifica(Vx,Vy):
        copia= copy.deepcopy(matriz)
        m=copia[x][y]
        copia[x][y]=copia[Vx][Vy]
        copia[Vx][Vy]=m
        jogadas.append(copia)

    #esquerda
    Vx=x
    Vy=y-1
    if verifica(Vx,Vy):
        copia= copy.deepcopy(matriz)
        m=copia[x][y]
        copia[x][y]=copia[Vx][Vy]
        copia[Vx][Vy]=m
        jogadas.append(copia)

    return jogadas


#Função para localizar o espaço vazio
def localizar(matriz,valor):
    for i in range (3):
        for j in range (3):
            if matriz[i][j] == valor:
                return i,j

#Heuristica distância de Manhattan
def distaciaDeManhattan(matriz,resposta):
    dist =0
    for i in matriz:
        for j in i:
            #if not (j=='0'):#Não considera a movimentação da pedra branca
                xAtual,yAtual= localizar(matriz,j)
                xCorreto,yCorreto= localizar(resposta,j)
                distancia=abs(int(xAtual-xCorreto))+abs(int(yAtual-yCorreto))#Distancia de Manhattan
                dist+=distancia
    
    
    return dist

def menorSomatorio(filhos):
    distanciasDosFilhos = []
    for i in filhos:
        distanciasDosFilhos.append(distaciaDeManhattan(i,resposta))
    #print("Vetor de distancia dos filhos")
    #print(distanciasDosFilhos)
    posVet = distanciasDosFilhos.index(min(distanciasDosFilhos))
    return filhos[posVet] #retorna o filho que tem a menor distancia das peças

#Número de elementos na posição errada
def posicaoErrada(matriz,resposta):
    cont=0
    for i in range(3):
        for j in range(3):
            if matriz[i][j]!= resposta[i][j]:
                cont+=1
    return cont

    

"""
def buscaEmProfundidade(matriz):
    nivel=0#Profundidade dos nós
    noNaoVisitado=[matriz]#pilha que começa com o primeiro nó
    custoDeEspaco=0
    while(len(noNaoVisitado)>0):
        pai=noNaoVisitado.pop()#elemento do topo da pilha 

        if (numpy.array_equal(pai,resposta)):
            print("Solucao encontrada")
            
        
        nivel+=1
        jogadasPossiveis=movimento(pai) #retorna os filhos possiveis do pai
        custoDeEspaco+=len(jogadasPossiveis)#Todos os filhos gerados
        shuffle(jogadasPossiveis)#Embaralha os filhos 

        noNaoVisitado.append(jogadasPossiveis[0])#adiciona o nó mais a esquerda


def buscaEmLargura():
    pass
"""
#Busca gulosa utilizando como fronteira apenas os filhos de um pai que foi escolhido pela distÂncia de manhattan
def buscaHeuristica(matrizPai,resposta):
    custoDeEspaco=0
    nivel=0#Nível da árvore
    visitados=[matrizPai]#Começa com o pai
    while(True):
        if(numpy.array_equal(matrizPai,resposta)):
            print("Solucao encontrada")
            break
        nivel+=1
        jogadasPossiveis=[]
        for filho in movimento(matrizPai):
            if filho not in visitados:
               #visitados.append(filho)
                jogadasPossiveis.append(filho)
                #visitados.append(filho)
        print("Tamanho dos visitados = "+str(len(visitados)))
        custoDeEspaco+=len(jogadasPossiveis)#Todos os filhos gerados
        try:
            matrizPai=menorSomatorio(jogadasPossiveis)#Retorna o filho com as peças menos distantes
            imprimindoTablueiro(matrizPai)
            
        except:
            print("NAO POSSUI SOLUCAO")
            break
        visitados.append(matrizPai)
              
#Busca gulosa com fronteira muito grande são todos os nós que ainda não foram expandidos
def busca_heuristica2(matrizPai,resposta):
    h = []
    heappush(h,(distaciaDeManhattan(matrizPai,resposta),matrizPai))#Adiciona os elementos a heap  (distancia de manhattan , nó)
    visitados = [matrizPai]
    cont=0
    while (len(h)>0):
        cont+=1
        print("\n"+str(cont)+"\n")
        (_,pai) = heappop(h)
        imprimindoTablueiro(pai)

        for filho in movimento(pai):
            if filho not in visitados:
                visitados.append(filho)
                if filho == resposta:
                    print("Solução encontrada")
                    print(len(visitados))
                    return 
                else:
                    heappush(h,(distaciaDeManhattan(filho,resposta),filho))

    print("Sem Solucao")





# Função de conversão para str
def son2str(s):
    s1 = s[0] + s[1] + s[2]
    return ''.join([str(v) for v in s1])

def busca_a_Star(start,goal,heuristica):
    h = []
    heappush(h,(heuristica(start, goal), start))
    pais = dict()
    visited = [start]
    cont=0
    while (len(h) > 0):
        cont+=1
       # print(cont)
        (_, pai) = heappop(h)#Retira o menor elemento da heap
        for filho in movimento(pai):
            if filho not in visited:
                visited.append(filho)
                pais[son2str(filho)] = pai
                no = filho
                profund = 0
                while no != start:
                    no = pais[son2str(no)]
                    profund += 1
                if filho == goal:
                    print(len(visited))
                    print("Solução encontrada")
                    return 
                else:
                    heappush(h, (heuristica(filho, goal)+ profund, filho))#Adiciona os itens na heap((distancia)+profundidade , filho)
    print("Nao tem solucao")



#matriz=criandoTabuleiro()
#imprimindoTablueiro(matriz)
lances=movimento(matriz)
#print(lances)
#custo=distanciaDosMovimentos(matriz,resposta)
#buscaEmProfundidade(matriz)

buscaHeuristica(matriz,resposta)

busca_heuristica2(matriz,resposta)
busca_a_Star(matriz,resposta,distaciaDeManhattan)


 