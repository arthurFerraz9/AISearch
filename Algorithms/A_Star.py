class A_Star:

    def __init__(self, heuristic, problem, vocabulary=[], word_cost=10):
        self.heuristic = heuristic
        self.problem = problem
        self.vocabulary = vocabulary
        self.word_cost = word_cost

    def execute(self):
        node = make_node(self.problem)
        frontier = [node]
        explored = []
        while True:
            if len(frontier) == 0:
                return None
            node = frontier.pop()
            print(node.state)

            if self.problem.goal_test(node.state):
                return node.state

            for word in self.vocabulary:
                if word not in node.state:
                    child = get_child_node(node, word)
                    if child.state not in explored and child.state not in frontier:
                        frontier.append(child)

            frontier = sorted(frontier, key=lambda node: self.evaluate(node), reverse=True)

    def evaluate(self, node):
        return len(node.state)*self.word_cost - self.heuristic.value_of(node.state)


class Node:

    def __init__(self, state, father):
        self.state = state
        self.father = father


def make_node(problem):
    node = Node(problem.get_initial_state(), None)
    return node


def get_child_node(node, word):
    child_node = Node(list(node.state), node)
    child_node.state.append(word)
    return child_node
