"""
Extract keypoints from a sentence
"""
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk import ne_chunk
from nltk import pos_tag
from re import sub

# global list of stop words
STOPWORDS = set(stopwords.words("english"))
# global list of recommended clubs
CLUBS = ["AIESEC", "Rotract", "Gavel", "LED", "LEO", "Mora SPIRIT", "IEASL",
         "Interact", "Model United Nations", "Moot Court"]
PROF = ["CIMA", "CIM", "ACCA", "CA", "SLIM", "AAT", "MBA", "MSC", "PQHRM",
        "Banking", "LLB", "BSC"]


def cleanup_bulletpoints(sentence):
    """Removes non alphanumeric characters
    from the sentence
    """
    return sub('[^A-Za-z0-9]+', ' ', sentence)

def cleanup_brackets(sentence):
    """Helper function for advanced_search_tree_sport
    Removes words and character inside
    brackets
    """
    brackets_removed = sub(r'\(.*?\)', ' ', sentence)
    return cleanup_bulletpoints(brackets_removed)

def cleanup_sentence(sentence):
    """Removes stopwords and unnecessary tags
    from the sentence
    """
    global STOPWORDS
    words = word_tokenize(sentence)
    filter_sentence = [w for w in words if w not in STOPWORDS]
    return " ".join(w for w in filter_sentence)

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


def calculate_score_qualification(sentence):
    """search if any keyword is mentioned in the
    sentence (normal)
    """
    global PROF
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


def advanced_search_tree_sport(sentence):
    """Return True if the sentence is "GPE" else False
    """
    words = word_tokenize(sentence)
    tagged = pos_tag(words)
    namedEnt = ne_chunk(tagged)
    tree = list({(" ".join(c[0] for c in chunk), chunk.label())
                 for chunk in namedEnt if hasattr(chunk, 'label')})
    for name, entity in tree:
        if entity == "GPE":
            return True
        else:
            return False


def advanced_search_sport(sentence):
    """Return a (advanced) score which is calculated using
    counting the number of words which represent a sport ("GPE")
    """
    word_list = word_tokenize(sentence)
    advanced_score = 0
    for word in word_list:
        temp_score = advanced_search_tree_sport(word)
        if temp_score == True:
            advanced_score += 1
    return advanced_score


def calculate_score_sport(adv_score, nor_score):
    """calculates the score by comparing (average)
    the advanced score and the normal score
    arguments:
        adv_score -> score obtained from advanced_search_sport
        nor_score -> number of words in the filtered_sentenced
    """
    avg_score = (adv_score + nor_score) // 2
    if avg_score >= 5:
        return 3
    elif 5 > avg_score >= 3:
        return 2
    else:
        return 1

def sports_main(sentence):
    """Returns a score
    add more here
    """
    sentence = cleanup_brackets(sentence)
    filter_sentence = cleanup_sentence(sentence)
    adv_score = advanced_search_sport(sentence)
    nor_score = len(word_tokenize(filter_sentence))
    return calculate_score_sport(adv_score, nor_score)
