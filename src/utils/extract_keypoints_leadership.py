from nltk.tokenize import word_tokenize
from .clean_sentences import cleanup_sentence, cleanup_bulletpoints,\
        cleanup_brackets


def calculate_score_leadership(sentence):
    """Returns the score of the given sentence
    according to the keywords present in the
    sentence
    """
    # group 1 score is 1.5
    group_1 = {"President", "Captain", "Leader"}
    # group 2 score is 1.0
    group_2 = {"Team Leader", "Treasurer"}
    # group 3 score is 0.5
    group_3 = {"Secretory", "prefect", "active member"}
    word_set = set(word_tokenize(sentence))
    s1 = len(word_set.intersection(group_1)) * 1.5
    s2 = len(word_set.intersection(group_2))
    s3 = len(word_set.intersection(group_3)) * 0.5
    score = s1 + s2 + s3
    return score


def leadership_main(sentence):
    """
    """
    sentence = cleanup_bulletpoints(cleanup_brackets(sentence))
    filter_sentence = cleanup_sentence(sentence)
    return calculate_score_leadership(filter_sentence)
