from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag

wordnet_tags = ['n', 'v']
corpus = [
    'He ate the sandwiches',
    'Every sandwich was eaten by him'
]

stemmer = PorterStemmer()
print('Stemmed: {0}'.format(
    [[stemmer.stem(token) for token in word_tokenize(doc)] for doc in corpus]
))

lemmatizer = WordNetLemmatizer()
def lemmatize(token, tag):
    if tag[0].lower() in wordnet_tags:
        return lemmatizer.lemmatize(token, tag[0].lower())
    return token

tagged_corpus = [pos_tag(word_tokenize(doc)) for doc in corpus]
print('Lemmatized: {0}'.format(
    [[lemmatize(token, tag) for token, tag in doc] for doc in tagged_corpus]
))