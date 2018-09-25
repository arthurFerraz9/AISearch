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
            random_gene = self.generate_random_gene(vocabulary)
            self.genes.append(random_gene)
        self.fitness = self.calculate_fitness(heuristic)

    def generate_random_gene(self, vocabulary):
        candidate_gene = sample(vocabulary, 1)[0]
        while (candidate_gene in self.genes):
            candidate_gene = sample(vocabulary, 1)[0]
        return candidate_gene

    def calculate_fitness(self, heuristic):
        return heuristic.value_of(self.genes)

    def mutate(self, heuristic, vocabulary):
        mutation_index = randint(0, len(self.genes) - 1)
        random_gene = self.generate_random_gene(vocabulary)
        self.genes[mutation_index] = random_gene
        self.fitness = self.calculate_fitness(heuristic)

