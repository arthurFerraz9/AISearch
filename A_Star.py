class A_Star:

    def __init__(self, heuristic, problem):
        self.heuristic = heuristic
        self.problem = problem

    def execute(self):
        node = make_node(self.problem)
        pathCost = 0
        frontier = [node]
        explored = []
        while True:
            node = frontier.pop()
            if self.problem.goal_test(solution(node)):
                return solution(node)
            if len(frontier) == 0:
                return None
            explored.append(node)
            for action in self.problem.actions(node.state):
                child = get_child_node(node, action)
                if child.state not in explored and child.state not in frontier:
                    frontier.append(child.state)
                return None


class Node:

    def __init__(self, state, father):
        self.state = state
        self.father = father


def make_node(problem):
    node = Node(problem.get_initial_state(), None)
    return node


def get_child_node(node, action):
    child_node = Node()
    #child_node.state = action(node.state)
    child_node.father = node
    return child_node


def solution(node):
    sentence = []
    while node is not None:
        sentence.insert(0, node.state)
        node = node.father
    return sentence
