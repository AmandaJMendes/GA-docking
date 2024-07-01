from docking import *

p_counts  = [50, 100, 1000]

elites    = [0, 5, 10]
r_parents = [0.0, 0.4, 0.8]
mutate    = [0.0, 0.01, 0.5]
Ns        = [10, 15, 20, 25]
N=10

# ps = [1, 10, 100, 1000, 5000]
# L = 1000
# N = 20
# navios = None
# for p in ps:
#     print(p)
#     result_ga        = solve_ga(N, L, p, 1000, navios = navios)
#     navios = result_ga[0]
#     #result_brutefoce = solve_bruteforce(result_ga[0], L)    
#     evaluate(result_ga)#, result_brutefoce, f'teste_{N}')
#     print('\n\n')
    
    # testar para número de navios diferentes fitness, tamanho e tempo (ag e força bruta), fazer early stopping no ag
    #


N = 20
L = 1000
p = 100
navios = None
for e in elites:
    for r in r_parents:
        for m in mutate:
            if (e < 5) and (r<0.1):
                continue
            print(e, r, m, end='    ')
            result_ga        = solve_ga(N, L, p, 1000, e, r, m, navios=navios)
            navios = result_ga[0]
            evaluate(result_ga)
result_brutefoce = solve_bruteforce(result_ga[0], L)
print(result_brutefoce)