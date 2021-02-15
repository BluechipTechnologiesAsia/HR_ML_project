from nltk.tokenize import word_tokenize
from nltk import ne_chunk
from nltk import pos_tag
from .clean_sentences import cleanup_sentence, cleanup_bulletpoints

# global list of recommended clubs
PROF = ["CIMA", "CIM", "ACCA", "CA", "SLIM", "AAT", "MBA", "MSC", "PQHRM",
        "Banking", "LLB", "BSC"]


def calculate_score_qualification(sentence):
    """search if any keyword is mentioned in the
    sentence (normal)
    """
    global PROF
    score = 0
    for word in word_tokenize(sentence):
        if word in PROF[:3]:
            score += 1.5
        elif word in PROF[3:6]:
            score += 1.0
        elif word in PROF[6:]:
            score += 0.5
        else:
            pass
    return score


def advanced_search_qualification(sentence):
    """search if any keyword is mentioned in the
    sentence (advanced) and gives a score to the
    sentence.
    - scoring -
    check calculate_score_qualification function
    """
    score = 0
    words = word_tokenize(sentence)
    tagged = pos_tag(words)
    namedEnt = ne_chunk(tagged)
    tree = list({(" ".join(c[0] for c in chunk), chunk.label())
                 for chunk in namedEnt if hasattr(chunk, 'label')})
    for name, entity in tree:
        if entity == "ORGANIZATION":
            score += calculate_score_qualification(name)
    return (5 if score > 5 else score)


def prof_qualification_main(sentence):
    """
    add something here
    """
    sentence = cleanup_bulletpoints(sentence)
    filter_sentence = cleanup_sentence(sentence)
    return advanced_search_qualification(filter_sentence)
