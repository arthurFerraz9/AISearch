from vocabulary.vocabulary import Vocabulary as vb


def import_text(file_path):
    with open(file_path, "r") as text_file:
        text = text_file.read()
    for non_desirable_character in ['“', '”', '\n', '.', ',', '!', '?']:
        text = text.replace(non_desirable_character, '')
    vocabulary = text.split(" ")
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