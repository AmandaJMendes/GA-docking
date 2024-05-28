"""
Autor: Victor Barros Coch
Trabalho 1 - Problema da Mochila """

from genetic2022 import *

def run_bruteforce(itens, peso_max):
    n_itens = len(itens)
    #Individuo inicial (todos zeros)
    individuo = BitArray(n_itens)
    #Individuo final (todos uns)
    end = BitArray(n_itens)
    end.invert()
    #Contador de combinacoes
    combos = 0

    #Verifica todos possiveis individuos
    best = (0,individuo)
    while individuo.uint < end.uint:
        individuo = BitArray(uint = individuo.uint+1, length=n_itens)
        fit = fitness(individuo ,itens ,peso_max)

        if fit > best [0]:
            best = (fit, individuo)
        combos += 1

    print("Nro de combinacoes (Brute Force): "+str(combos))
    return(best)
