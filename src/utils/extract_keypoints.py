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
CLUBS = ["AIESEC", "Rotract", "Gavel", "LED", "LEO", "Mora SPIRIT", "IEASL", "Interact", "Model United Nations", "Moot Court"] 

def cleanup_bulletpoints(sentence):
    """Removes non alphanumeric characters
    from the sentence
    """
    return sub('[^A-Za-z0-9]+', ' ', sentence)


def cleanup_sentence(sentence):
    """Removes stopwords and unnecessary tags
    from the sentence
    """
    global STOPWORDS
    words = word_tokenize(sentence)
    filter_sentence = [w for w in words if w not in STOPWORDS]
    return " ".join(w for w in filter_sentence)


def normal_search(sentence):
    """search if any keyword is mentioned in the
    sentence (normal)
    """
    score = 0
    keyword = set(["AISEC"])
    if keyword in word_tokenize(sentence):
        score += 1
    return score


def advanced_search(sentence):
    """search if any keyword is mentioned in the 
    sentence (advanced)
    TODO: edit this part
    """
    words = word_tokenize(sentence)
    tagged = pos_tag(words)
    namedEnt = ne_chunk(tagged)
    return {(" ".join(c[0] for c in chunk), chunk.label())for chunk in namedEnt if hasattr(chunk,'label')}

if __name__ == "__main__":
    sentence = """Vice President(External Relations)- Blue Marble Project- AIESEC University of Peradeniy Vice President, Committee member - Human Resource Guild - Faculty of Management - University of Peradeniya Active member of AIESEC University of Peradeniya A member of the Rotaract Club - University of Peradeniya Member of Faculty Toastmasters Club Senior committee member - Broadcasting Unit - Visakha Vidyalaya Junior prefect Vice President - English Literary Association Committee member - School Buddhist Association Member of school debating and Shakespeare drama crew
    """
    filter_sentence = cleanup_sentence(cleanup_bulletpoints(sentence))
    print(advanced_search(filter_sentence))
    
