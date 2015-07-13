from sklearn.feature_extraction.text import HashingVectorizer

corpus = ['the', 'ate', 'bacon', 'cat']
vec = HashingVectorizer(n_features=6)
print(vec.transform(corpus).todense())
