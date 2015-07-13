# lemmatization
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('gathering', 'v'))  # gather
print(lemmatizer.lemmatize('gathering', 'n'))  # gathering

print(lemmatizer.lemmatize('eats', 'v'))  # eat
print(lemmatizer.lemmatize('ate', 'v'))  # eat
print(lemmatizer.lemmatize('eaten', 'v'))  # eat

# stemming
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem('gathering'))  # gather
print(stemmer.stem('eats'))  # eat
print(stemmer.stem('ate'))  # ate
print(stemmer.stem('eaten'))  # eaten

