from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from re import sub

# global list of stop words
STOPWORDS = set(stopwords.words("english"))


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
