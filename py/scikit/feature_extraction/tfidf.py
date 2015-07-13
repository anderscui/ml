from sklearn.feature_extraction.text import CountVectorizer

corpus = ['The dog ate a sandwich, the wizard transfigured a sandwich, and I ate a sandwich']
vec = CountVectorizer(stop_words='english')
print(vec.fit_transform(corpus).todense())
print(vec.vocabulary_)

# [[2 1 3 1 1]]
# {u'sandwich': 2, u'wizard': 4, u'dog': 1, u'transfigured': 3, u'ate': 0}

from sklearn.feature_extraction.text import TfidfVectorizer

corpus = ['The dog ate a sandwich and I ate a sandwich',
          'The wizard transfigured a sandwich'
          ]

vec = TfidfVectorizer(stop_words='english')
print(vec.fit_transform(corpus).todense())
print(vec.vocabulary_)
