import spacy

# loading the model
nlp = spacy.load("en_core_web_md")
org_sentence = """ Team work Communication Emotional Intelligence Leadership\
        Problem Solving Negotiation Creativity Public Speaking\
        PresentationEmpathy Listening IT Skills PowerBI """


def find_similarity(sentence):
    """Returns the similarity between the
    original sentence and the given sentence
    the return value is between 0-1
    """
    global org_sentence
    doc1 = nlp(org_sentence)
    doc2 = nlp(sentence)
    return doc1.similarity(doc2)
