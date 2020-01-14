import numpy as np
import random
import sys
sys.path.append ('chrome_trex.zip')

from chrome_trex import DinoGame



CHANCE_MUT = .20
CHANCE_CO = .25
NUM_INDIVIDUES = 15
NUMBERS = 3


def sort_list (list, sort, descending = true):
return[x for _,x in sorted(zip(sort, list),key = lambda p:p [0],reverse=descending)]


def population_random (n):
population = []
for i in range (n):
    populacao.append (np.random.uniform (-10, 10, (3, 10)))
    return population


def action_value (individual, state):


    return individual @ state


best_player (individual, state):


    return np.argmax (action_value (individual, state))


def mutation (individual):


    for i in range (3):
        for j in range (10):
            if np.random.uniform (0, 1) <CHANCE_MUT:
                individual [i] [j] * = np.random.uniform (-1.5, 1.5)


def crossover (individual1, individual2):

    child = individual1.copy ()
    for i in range (3):
        for j in range (10):
            if np.random.uniform (0, 1) <CHANCE_CO:
                child [i] [j] = individual2 [i] [j]
    return son


def calculate_fitness (game, individual):


    game.reset ()
    while not game.game_over:
        state = game.get_state ()
        action = best_played (individual, state)
        game.step (action)
    return game.get_score ()


def next_generation (population, fitness):

    wages = list_list (population, fitness)
    proxima_ger = ordered [: NUMBERS]


    while len (next_ger) <NUM_INDIVIDUES:

        ind1, ind2 = random.choices (population, k = 2)
        child = crossover (ind1, ind2)
        mutation (son)
        proxima_ger.append (child)

    return next_ger


def show_best_individual (game, population, fitness):


    fps_old = game.fps
    game.fps = 100
    ind = population [max (range (len)), key = lambda i: fitness [i])]
    print ('Best Guy:', ind)
    while True:
        if input ('Press enter to run the best agent. Type q to exit.') == 'q':
            game.fps = fps_old
            return
        fit = calculate_fitness (game, ind)
        print ('Fitness: {: 4.1f}'. format (game.get_score ()))



num_generations = 100
game = DinoGame (fps = 50_000)

population = random_population (NUM_INDIVIDUES)

print ('ger | fitness \ n ---- + -' + '-' * 5 * NUM_INDIVIDUES)

for ger in range (num_generations):
    fitness = []
    for ind in population:
        fitness.append (calculate_fitness (game, ind))

    population = next_generation (population, fitness)

    print ('{: 3} |' .format (ger),
          '' .join ('{: 4d}'. format (s) for s in sorted (fitness, reverse = True)))
fitness = []
for ind in population:
    fitness.append (calculate_fitness (game, ind))

show_best_individual (game, population, fitness)
