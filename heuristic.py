class Heuristic:

    def __init__(self, file_of_meanings):
        self.word_classificator = {}
        with open(file_of_meanings, "r") as classifier:
            lines = classifier.readlines()
            for line in lines:
                word, kind = line.split(':')
                kind = kind.replace('\n','')
                self.word_classificator[word] = kind

        self.rules = {
            'noun': ['adjective', 'definite-article', 'indefinite-article', 'verb-transitive', 'pronoun'],
            'noun-plural': ['adjective', 'definite-article', 'indefinite-article', 'verb-transitive', 'pronoun'],
            'proper-noun' : ['adjective', 'definite-article', 'indefinite-article', 'verb-transitive', 'pronoun'],
            'adjective' : ['definite-article', 'indefinite-article', 'verb-transitive', 'pronoun'],
            'definite-article' : ['adjective', 'verb-transitive', 'pronoun'],
            'indefinite-article' : ['adjective', 'verb-transitive', 'pronoun'],
            'preposition' : ['verb-transitive', 'verb-intransitive', 'verb', 'auxiliary verb'],
            'conjunction' : ['verb-transitive', 'verb-intransitive', 'verb', 'auxiliary verb'],
            'adverb' : ['verb-transitive', 'verb-intransitive', 'verb', 'auxiliary verb'],
            'verb-transitive' : ['noun', 'adverb', 'conjunction'],
            'verb-intransitive' : ['noun', 'adverb', 'conjunction'],
            'verb' : ['noun', 'adverb', 'conjunction'],
            'auxiliary-verb' : ['noun', 'adverb', 'conjunction']
        }


    def value_of(self, phrase):
        value = 0
        first_word = phrase[0]
        if self.word_classificator[first_word] == 'noun':
            value += 5
        for current_word_index in range (1, len(phrase)):
            current_word_class = self.word_classificator[phrase[current_word_index]]
            before_word_class = self.word_classificator[phrase[current_word_index-1]]

            if before_word_class in self.rules.get(current_word_class,[]):
                value += 7
        return value


