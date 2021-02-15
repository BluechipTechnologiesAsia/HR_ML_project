import spacy

# loading the model
nlp = spacy.load("en_core_web_md")
org_sentence = """Plan good Society Happiness Energy Focus Future Service
Navigate Impact Sustainability Legacy Unique Authentic Better Safe """


def find_similarity(sentence):
    """Returns the similarity between the
    original sentence and the given sentence
    the return value is between 0-1
    """
    global org_sentence
    doc1 = nlp(org_sentence)
    doc2 = nlp(sentence)
    return doc1.similarity(doc2)
