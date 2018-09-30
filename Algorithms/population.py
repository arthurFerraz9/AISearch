from Algorithms.individual import Individual

class Population:

    def __init__(self, size, individual_size):
        self.individuals = []
        self.size = size
        self.individual_size = individual_size
        self.total_fitness = 0

    def generate_random(self, heuristic, vocabulary):
        for i in range(self.size):
            self.individuals.append(Individual(self.individual_size))
            new_individual = self.individuals[i]
            new_individual.generate_random_genes(heuristic, vocabulary)
            self.total_fitness += new_individual.fitness

    def add_individual(self, individual):
        self.individuals.append(individual)
        self.total_fitness += individual.fitness

    def get_best(self):
        best = None
        best_fitness = 0
        for individual in self.individuals:
            if individual.fitness > best_fitness:
                best_fitness = individual.fitness
                best = individual
        return best
