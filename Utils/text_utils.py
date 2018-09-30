from vocabulary.vocabulary import Vocabulary as vb
from nltk import word_tokenize, pos_tag

non_desirable_characters = ['"', '"', '\n', '.', ',', '!', '?', ';', "''", ':', '``']

def import_text(file_path):
    with open(file_path, "r") as text_file:
        text = text_file.read()
    for non_desirable_character in non_desirable_characters:
        text = text.replace(non_desirable_character, '')
    vocabulary = text.split(" ")
    return set(vocabulary)

def genetic_import_text(file_path):
    vocabulary = []
    with open(file_path) as text_file:
        raw = text_file.read()
    tokens = word_tokenize(raw)
    for token in tokens:
        if token not in non_desirable_characters:
            vocabulary.append(token)
    return set(vocabulary)

def create_classifier(file_path, vocabulary):
    with open(file_path, "w") as classifier:
        for word in vocabulary:
            classifier.writelines(word + ':' + get_classification(word)+ '\n')


def get_classification(word):
    full_meaning = vb.part_of_speech(word, format='dict')
    classification = None
    if full_meaning:
        classification = full_meaning[0]['text']
    if classification is None:
        classification = ''
    return classification

def create_nltk_classifier(classifier_path, base_text_path):
    with open(base_text_path, "r") as base_text_file:
        raw = base_text_file.read()
    tokens = word_tokenize(raw)
    tagged_tokens = list(set(pos_tag(tokens)))

    with open(classifier_path, "w") as classifier:
        for tagged_token in tagged_tokens:
            if tagged_token[0] not in non_desirable_characters:
                classifier.write(tagged_token[0] + ":" + tagged_token[1] + "\n")