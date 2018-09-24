from random import randint
from population import Population
from individual import Individual


class Genetic:

    def __init__(self, heuristic, problem, vocabulary):
        self.population_size = 100
        self.individual_size = problem.max_size_of_sentence
        self.heuristic = heuristic
        self.vocabulary = vocabulary
        self.population = Population(self.population_size, self.individual_size)
        self.population.generate_random(heuristic, vocabulary)

    def execute(self):
        for i in range(1000):
            new_population = Population(self.population_size, self.individual_size)
            for j in range(len(self.population.individuals)):
                first_parent = self.select_individual()
                second_parent = self.select_individual()
                child = self.reproduce(first_parent, second_parent)
                child = self.check_for_mutation(child)
                new_population.add_individual(child)
            self.population = new_population
            print("Iteration %d..." % i)
        print(self.population.get_best().genes)

    def select_individual(self):
        choice = randint(0, max(0, self.population.total_fitness - 1))
        fitness_sum = self.population.individuals[0].fitness
        current_index = 0
        individual = self.population.individuals[current_index]
        while fitness_sum < choice:
            current_index += 1
            fitness_sum += self.population.individuals[current_index].fitness
            individual = self.population.individuals[current_index]
        return individual

    def reproduce(self, fp, sp):
        fp_size = len(fp.genes)
        crossover_index = randint(0, fp_size - 1)
        child = Individual(fp_size, genes=fp.genes[0:crossover_index] + sp.genes[crossover_index:len(sp.genes)], heuristic=self.heuristic)
        return child

    def check_for_mutation(self, child):
        p = 3
        if randint(0, 99) < p:
            child.mutate(self.heuristic, self.vocabulary)
        return child


