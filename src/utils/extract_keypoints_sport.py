from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from .clean_sentences import cleanup_sentence, cleanup_bulletpoints,\
        cleanup_brackets


def check_present(sentence):
    """Helper Function for is_it_sport
    """
    hypernyms = ["sport", "game"]
    for hyper in hypernyms:
        if hyper in sentence:
            return True
    return False


def is_it_sport(sentence):
    """Return True if the (sentence) is a sport
    """
    word = word_tokenize(sentence)
    for w in word:
        # capitalizing the word
        w = w.capitalize()
        try:
            syns = wordnet.synsets(w)
            word_hyper = syns[0].hypernyms()
            word_hypo = syns[0].hyponyms()
            for w in word_hyper:
                if check_present(w.name()):
                    return True
            for w in word_hypo:
                if check_present(w.name()):
                    return True
        except IndexError:
            pass
    return False


def advanced_search_sport(sentence):
    """
    """
    word_list = word_tokenize(sentence)
    advanced_score = 0
    for word in word_list:
        temp_score = is_it_sport(word)
        if temp_score:
            advanced_score += 1
    return advanced_score


def sports_main(sentence):
    """Main function
    Returns advanced score
    """
    sentence = cleanup_brackets(sentence)
    filter_sentence = cleanup_sentence(cleanup_bulletpoints(sentence))
    adv_score = advanced_search_sport(filter_sentence)
    return adv_score
