import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

UNWANTED_CHARS = set(string.punctuation) | set("\n\t\r")

en_stopwords = set(stopwords.words('english'))


def clean_text(text):
    chars = [char for char in text.lower() if char not in UNWANTED_CHARS]

    no_punc_text = ''.join(chars)

    words = [word for word in no_punc_text.split(' ') if not (len(word) == 0 or
                                                              word in en_stopwords or
                                                              word.isspace() or
                                                              word.isnumeric())]

    return ' '.join(words)
