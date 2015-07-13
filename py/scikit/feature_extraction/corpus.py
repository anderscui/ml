corpus = [
    'UNC played Duke in basketball played',
    'Duke lost the basketball game',
    'I ate a sandwich'
]

# bag-of-words presentation
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(binary=True)
print(vectorizer.fit_transform(corpus).todense())
print(vectorizer.vocabulary_)
# [[0 1 1 0 1 0 1 0 0 1]
#  [0 1 1 1 0 1 0 0 1 0]
#  [1 0 0 0 0 0 0 1 0 0]]

# distance
from sklearn.metrics.pairwise import euclidean_distances
counts = vectorizer.fit_transform(corpus).todense()
print('Distance between 1st and 2nd docs: {0}'.format(euclidean_distances(counts[0], counts[1])))
print('Distance between 1st and 2nd docs: {0}'.format(euclidean_distances(counts[0], counts[2])))
print('Distance between 1st and 2nd docs: {0}'.format(euclidean_distances(counts[1], counts[2])))

# stop words
sw_vec = CountVectorizer(stop_words='english')
print(sw_vec.fit_transform(corpus).todense())
print(sw_vec.vocabulary_)