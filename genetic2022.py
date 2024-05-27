"""
Autor: Victor Barros Coch
Adaptado de genetic2020.py
Trabalho 1 - Problema da Mochila """

from random import randint , random , getrandbits
from operator import add
from functools import reduce
from bitstring import BitArray

def individual(length , rand=True):
    #Cria um membro da populacao, array de bits aleatorios
    if rand:
        return BitArray(uint=getrandbits(length) ,length=length)
    else:
        return BitArray(length)

def population(count, length):
    #Cria a populacao
    return [ individual(length) for x in range(count) ]

def fitness(individual , itens , peso_max):
    """
    O fitness do individuo sera a soma dos valores contidos na mochila. ZERO no caso de ultrapassar o peso maximo.
    """

    #Valores iniciais
    peso = 0
    valor = 0

    #Para cada bit
    for i,x in enumerate(individual):
        #Se estiver contido na mochila
        if x :
            peso += itens[i][0]
            valor += itens[i][1]

            #Se exceder o peso maximo
            if peso > peso_max:
                return 0
    return valor

def peso(individual , itens):
    peso =0
    for i,x in enumerate(individual):
        if x:
            peso+=itens[i][0]
    return peso


def media_fitness(pop, itens, peso_max):
    #Media de fitness da populacao
    summed = reduce(add, (fitness(x, itens, peso_max) for x in pop))
    sum_peso = 10*reduce(add, (peso(x,itens) for x in pop))
    len_ = len(pop)*1.0
    return (summed/len_, sum_peso/len_)

def best_fitness(pop, itens, peso_max):
    #Melhor fitness da populacao
    graded = [(x, fitness(x, itens, peso_max)) for x in pop]
    best = max(graded, key=lambda graded:graded[1])

    return (best[1], 10*peso(best[0], itens))

def evolve(pop, itens, peso_max, elite=5, r_parents=0.4, mutate=0.01):
    #Tabula cada individuo e o seu fitness
    graded = [(fitness(x, itens, peso_max), x) for x in pop]

    #Ordena for fitness
    graded = sorted(graded, key=lambda graded: graded[0], reverse=True)

    #Pais
    parents_length = int(len(graded)*r_parents)

    #Elitismo
    if elite:
        parents = [x[1] for x in graded][0:elite]
    else:
        parents = []

    #Roleta
    sum_fit = reduce(add, (x[0] for x in graded))
    while len(parents) < parents_length:
        pick = random ()
        acum_fit = 0
        for i, (fit, individual) in enumerate(graded):
            acum_fit += fit/sum_fit #Distribuicao acumulativa normalizada
            
            if acum_fit > pick:
                parents.append(individual)
                break

    parents_length = len(parents)
    #descobre quantos filhos terao que ser gerados alem da elite e aleatorios
    desired_length = len(pop) - parents_length
    children = []
    #comeca a gerar filhos que faltam
    while len(children) < desired_length:
        #escolhe pai e mae no conjunto de pais
        male = randint(0, parents_length -1)
        female = randint(0, parents_length -1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = randint(2,len(male))
            #gera filho metade de cada
            child = male[:half] + female[half:]
            #adiciona novo filho a lista de filhos
            children.append(child)

    #Adiciona lista de filhos na nova populacao
    parents.extend(children)
    # mutate some individuals
    for i, individual in enumerate(parents):
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
            individual.invert(pos_to_mutate)
    return parents
