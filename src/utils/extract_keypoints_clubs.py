from nltk.tokenize import word_tokenize
from nltk import ne_chunk
from nltk import pos_tag
from .clean_sentences import cleanup_sentence, cleanup_bulletpoints

# clubs
CLUBS = ["AIESEC", "Rotract", "Gavel", "LED", "LEO", "Mora Spirit",
         "IEASL", "Interact", "Model United Nations", "Moot Court"]


def calculate_score_clubs(sentence):
    """search if any keyword is mentioned in the
    sentence (normal)
    """
    global CLUBS
    score = 0
    for word in word_tokenize(sentence):
        if word in CLUBS[:3]:
            score += 1.5
        elif word in CLUBS[3:6]:
            score += 1.0
        elif word in CLUBS[6:]:
            score += 0.5
        else:
            pass
    return score


def advanced_search_clubs(sentence):
    """search if any keyword is mentioned in the
    sentence (advanced) and gives a score to the
    sentence.
    - scoring -
    check calculate_score_clubs function
    """
    score = 0
    words = word_tokenize(sentence)
    tagged = pos_tag(words)
    namedEnt = ne_chunk(tagged)
    tree = list({(" ".join(c[0] for c in chunk), chunk.label())
                 for chunk in namedEnt if hasattr(chunk, 'label')})
    for name, entity in tree:
        if entity == "ORGANIZATION":
            score += calculate_score_clubs(name)
    return (5 if score > 5 else score)


def clubs_main(sentence):
    """
    """
    sentence = cleanup_bulletpoints(sentence)
    filter_sentence = cleanup_sentence(sentence)
    return advanced_search_clubs(filter_sentence)
