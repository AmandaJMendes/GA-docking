"""
Código adaptado de mochila.py (de Victor Barros Coch Adaptado de SomaTarget.py)
"""

from matplotlib import pyplot as plt
from genetic2022 import *
from bruteforce import *
import time
import random
from flask import Flask, request, jsonify
from flask_cors import CORS

def solve_bruteforce(navios, L):
    """
    Parâmetros:
    - navios: Lista de navios
    - L: Comprimento máximo do cais

    Retorna:
    - Lista com os navios que devem dockar, segundo o algoritmo de força bruta
    - Tempo que a execução levou (em segundos)
    """
    # Calcula valor de validação com brute force
    t0 = time.time()
    best = run_bruteforce(navios, L)
    t1 = time.time()
    return best, t1-t0

def solve_ga(N, L, p_count, epochs):
    """
    Parâmetros:
    - N: Número de navios
    - L: Comprimento máximo do cais
    - p_count: Tamanho da população

    Retorna:
    - Lista de todos os navios aleatórios gerados
    - Lista com os navios que devem dockar, segundo o algoritmo genético
    - Lista contendo a evolução do fitness
    - Tempo que a execução levou (em segundos)
    """

    navios = [] # Definindo os navios (ln (comprimento), m (número de containers))
    for navio in range(N):
        ln = random.randint(1, L+1) # Comprimento do navio no intervalo [1, L]
        m  = random.randint(1, 100) # Número de containers no intervalo [1, 99]
        navios.append((ln, m))

    t0 = time.time() # Computar tempo para rodar o AG
    p = population(p_count , N) # Criando a população
    # Salva fitness para referência
    media  = media_fitness(p, navios, L)
    best_f = best_fitness (p, navios, L)
    fitness_history = [[media[0]],[media[1]],[best_f[0]],[best_f[1]]] # med fitness|med peso|best fitness|bets peso
    for i in range(epochs):
        p = evolve(p, navios , L)
        media  = media_fitness(p, navios, L)
        best_f = best_fitness (p, navios, L)
        fitness_history[0].append(media[0])
        fitness_history[1].append(media[1])
        fitness_history[2].append(best_f[0])
        fitness_history[3].append(best_f[1])
    t1 = time.time()
    best_individual = sorted(p, key=lambda p: p[0])[-1]
    best_individual_converted = [int(bit) for bit in best_individual]

    return navios, best_individual_converted, fitness_history, t1-t0

def evaluate(result_ga, result_brutefoce = None):
    """
    Essa função recebe os resultados dos algoritmos e plota as métricas
    """
    navios, p, fitness_history, t_ga = result_ga
    print("Tempo AG: "+str(t_ga))
    print("Individuo AG: "+str(sorted(p, key=lambda p:p[0])[-1])+", Valor: " +str(fitness_history[2][-1]))

    if result_brutefoce:
        best, t_bruteforce = result_brutefoce
        print("Tempo Brute Force: "+str(t_bruteforce))
        print("Individuo Brute Force: "+str(best[1])+", Valor: "+str(best[0]))
    

    fig = plt.figure()
    ax = plt.axes()

    ax.plot(fitness_history[0])
    ax.plot(fitness_history[2])
    if result_brutefoce:
        ax.plot([best[0] for i in fitness_history[0]])
    ax.plot(fitness_history[1])
    ax.plot(fitness_history[3])

    ax.legend(["Fitness Media", "Melhor Fitness", "Fitness Brute Force", " Peso Medio (x10)", "Peso do Melhor (x10)"])

    ax.grid(True)
    plt.show()


app = Flask(__name__)
CORS(app)

@app.route('/solve_ga', methods=['POST'])
def solve_ga_endpoint():
    data = request.json
    N = data['N']
    L = data['L']
    p_count = data.get('p_count', 1000)
    epochs = data.get('epochs', 1000)
    
    result_ga = solve_ga(N, L, p_count, epochs)
    navios, best_individual, fitness_history, t_ga = result_ga
    
    response = {
        "navios": navios,
        "best_individual": best_individual,
        "fitness_history": fitness_history,
        "time_ga": t_ga
    }
    
    return jsonify(response)

@app.route('/')
def hello_world():
    return "Hello World"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    # N = int(input("Número de navios: ")) # Número de navios
    # L = int(input("Comprimento do cais: ")) # Comprimento máximo do cais
        
    # p_count = 1000 # Tamanho da população
    # epochs  = 1000 # Número de gerações para testar

    # # Rodar algoritmos
    # result_ga        = solve_ga(N, L, p_count, epochs)
    # result_brutefoce = solve_bruteforce(result_ga[0], L)

    # # Plotar resultados
    # print()
    # print("Navios: ", result_ga[0])
    # evaluate(result_ga)#, result_brutefoce)