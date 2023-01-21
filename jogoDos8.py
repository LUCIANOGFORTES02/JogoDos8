import copy
import numpy 
from random import shuffle
#Criar tabuleiro
def imprimindoTablueiro(matriz):
    for i in range(0,3):
        print("|".join(matriz[i]))#unir as strings

        if(i<2):
            print("------")

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
                print ("[" + str(i) + "," + str(j) + "]")
                return i,j

#Heuristica distância de Manhattan
def distanciaDosMovimentos(matriz,resposta):
    dist =0
    for i in matriz:
        for j in i:
            xAtual,yAtual= localizar(matriz,j)
            xCorreto,yCorreto= localizar(resposta,j)
            distancia=abs(xAtual-xCorreto)+abs(yAtual-yCorreto)#Distancia de Manhattan
            dist+=distancia
    
    return dist


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


def menorSomatorio(filhos=[]):
    distanciasDosFilhos = []
    for i in filhos:
        distanciasDosFilhos.append(distanciaDosMovimentos(i))
    posVet = distanciasDosFilhos.index(min(distanciasDosFilhos))
    return filhos[posVet] #retorna o filho que tem a menor distancia das peças


def buscaHeuristica(matrizPai,resposta):
    custoDeEspaco=0
    nivel=0#Nível da árvore
    visitados=[matrizPai]#Começa com o pai
    while(True):
        if(numpy.array_equal(matrizPai,resposta)):
            print("Solucao encontrada")
        
        nivel+=1
        jogadasPossiveis=[]
        for filho in movimento(matriz):
            try:
                visitados.index(filho)
            except ValueError:
                jogadasPossiveis.append(filho)
                visitados.append(filho)
        
        custoDeEspaco+=len(jogadasPossiveis)#Todos os filhos gerados
        matrizPai=menorSomatorio(jogadasPossiveis)#Retorna o filho com as peças menos distantes
        for i in visitados:
            if(numpy.array_equal(matrizPai,i )):#Compara o pai com os que ja foram visitados para não entra em loop
                #pega outro filho
                pass










    


def A():
    pass

#Resultado esperado
resposta=[['1','2','3'],['4','5','6'],['7','8','0']]


matriz=criandoTabuleiro()
imprimindoTablueiro(matriz)
lances=movimento(matriz)
print(lances)
custo=distanciaDosMovimentos(matriz,resposta)
#buscaEmProfundidade(matriz)
buscaHeuristica(matriz,resposta)
print (custo)


 