import nltk

class Heuristic:

    def __init__(self, file_of_meanings, base_text_path=None):
        self.word_classificator = {}
        with open(file_of_meanings, "r") as classifier:
            lines = classifier.readlines()
            for line in lines:
                word, kind = line.split(':')
                kind = kind.replace('\n','')
                self.word_classificator[word] = kind
        if base_text_path is not None:
            with open(base_text_path) as base_text_file:
                raw = base_text_file.read()
                tokens = nltk.word_tokenize(raw)
            self.full_text = nltk.Text(tokens)

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

    def genetic_value_of(self, sentence):
        value = 0
        for i in range(len(sentence)):
            left_value = 0
            right_value = 0
            if i == 0:
                right_value = self.side_value_of(sentence, 0, 'r')
            elif i == len(sentence) - 1:
                left_value = self.side_value_of(sentence, -1, 'l')
            else:
                left_value = self.side_value_of(sentence, i, 'left')
                right_value = self.side_value_of(sentence, i, 'right')
            value += left_value + right_value
        return value

    def side_value_of(self, sentence, pos, side):
        side_pos = self.get_side_index(pos, side)
        concordance_list = self.full_text.concordance_list(sentence[pos])
        side_syntax_kind = self.word_classificator[sentence[side_pos]]
        qty_syntax_ocurrences = self.count_syntax_ocurrences(concordance_list, side, side_syntax_kind)
        return qty_syntax_ocurrences

    def get_side_index(self, pos, side):
        if side == 'right':
            return pos + 1
        else:
            return pos - 1

    def count_syntax_ocurrences(self, concordance_list, side, side_syntax_kind):
        counter = 0
        for concordance_line in concordance_list:
            line_classificator = nltk.pos_tag(nltk.word_tokenize(concordance_line.line))
            side_word = self.get_side_word_from_context(concordance_line, side)
            if (side_word, side_syntax_kind) in line_classificator:
                counter += 1
        return counter

    def get_side_word_from_context(self, concordance_line, side):
        side_word = ""
        if side == 'left' and len(concordance_line.left) != 0:
            side_word = concordance_line.left[-1]
        elif side == 'right' and len(concordance_line.left) != 0:
            side_word = concordance_line.right[0]
        return side_word

