"""
Autor: Victor Barros Coch Adaptado de SomaTarget.py
Trabalho 1 - Problema da Mochila
"""
from matplotlib import pyplot as plt
from genetic2022 import *
from bruteforce import *
import time

#Definindo itens possiveis (peso,valor)
itens = [(6 ,20) ,(5 ,12) ,(1 ,11) ,(1 ,55) ,(3 ,22) ,(8 ,80) ,(2 ,65) ,(3 ,27) ,(7 ,95) ,(17,28) ,(8,39) ,(2,86) ,(14,8) ,(5,84) ,(4,92) ,(3,73) ,(11,20) ,(3,14), (3 ,20) ,(5 ,18) ,(2 ,13) ,(8 ,35) ,(10 ,37) ,(7 ,78) ,(3 ,55)]

#Numero de intens
n_itens = len(itens)
print("Nro de itens: "+str(n_itens)) #Peso maximo da mochila
peso_max = 50

#Calcula valor de validacao com brute force
t0 = time.time()
best = run_bruteforce(itens, peso_max)
t1 = time.time()
print("Tempo Brute force: "+str(t1-t0))
t0 = time.time()

#Tamanho da populacao
p_count = 100

#Criando a populacao
p = population(p_count , n_itens)

#Numero de geracoes para testar
epochs = 1500

#Salva fitness para referencia
media = media_fitness(p, itens, peso_max)
best_f = best_fitness(p, itens, peso_max)
fitness_history = [[media[0]],[media[1]],[best_f[0]],[best_f[1]]] # med fitness|med peso|best fitness|bets peso

for i in range(epochs):
    p = evolve(p, itens , peso_max)
    media = media_fitness(p, itens, peso_max)
    best_f = best_fitness(p, itens, peso_max)
    fitness_history[0].append(media[0])
    fitness_history[1].append(media[1])
    fitness_history[2].append(best_f[0])
    fitness_history[3].append(best_f[1])

t1 = time.time()

print("Individuo Brute Force: "+str(best[1])+", Valor: "+str(best[0]))

print("Tempo AG: "+str(t1-t0))

print("Individuo AG: "+str(sorted(p, key=lambda p:p[0])[-1])+", Valor: " +str(fitness_history[2][-1]))

fig = plt.figure()
ax = plt.axes()

ax.plot(fitness_history[0])
ax.plot(fitness_history[2])
ax.plot([best[0] for i in fitness_history[0]])
ax.plot(fitness_history[1])
ax.plot(fitness_history[3])

ax.legend(["Fitness Media", "Melhor Fitness", "Fitness Brute Force", " Peso Medio (x10)", "Peso do Melhor (x10)"])

ax.grid(True)
plt.show()
