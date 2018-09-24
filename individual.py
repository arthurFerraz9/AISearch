from random import sample, randint


class Individual:

    def __init__(self, size, genes=None, heuristic=None):
        self.size = size
        if genes is None:
            self.genes = []
            self.fitness = 0
        else:
            self.genes = genes
            self.fitness = self.calculate_fitness(heuristic)

    def generate_random_genes(self, heuristic, vocabulary):
        for i in range(self.size):
            self.genes.append(sample(vocabulary, 1)[0])
        self.fitness = self.calculate_fitness(heuristic)

    def calculate_fitness(self, heuristic):
        return heuristic.value_of(self.genes)

    def mutate(self, heuristic, vocabulary):
        mutation_index = randint(0, len(self.genes) - 1)
        new_word = sample(vocabulary, 1)[0]
        self.genes[mutation_index] = new_word
        self.fitness = self.calculate_fitness(heuristic)

