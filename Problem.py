class SyntaxProblem:

    def __init__(self, max_size_of_sentence):
        self.max_size_of_sentence = max_size_of_sentence

    def goal_test(self, phrase):
        return len(phrase) == self.max_size_of_sentence

    def get_initial_state(self):
        return ""

    def get_actions(selfs):
        concat = list.append
        return concat
