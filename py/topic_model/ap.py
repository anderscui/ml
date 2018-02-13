# coding=utf-8
from __future__ import absolute_import, unicode_literals

import matplotlib.pyplot as plt
from gensim import corpora, models

corpus = corpora.BleiCorpus('../../data/ap/ap.dat', '../../data/ap/vocab.txt')

num_topics = 100
# bigger alpha maps to more topics for a doc.
model = models.LdaModel(corpus=corpus,
                        num_topics=num_topics,
                        id2word=corpus.id2word,
                        alpha=1.0)

doc = corpus.docbyoffset(0)
topics = model[doc]
print(topics)

# num_topics_used = [len(model[doc]) for doc in corpus]
# plt.hist(num_topics_used)
# plt.show()

# similarity of docs
from gensim import matutils

topics = matutils.corpus2dense(model[corpus], num_terms=model.num_topics)

from scipy.spatial import distance

# compute all the distances
pairwise = distance.squareform(distance.pdist(topics))
largest = pairwise.max()
for ti in range(len(topics)):
    pairwise[ti, ti] = largest + 1


def closest_to(doc_id):
    return pairwise[doc_id].argmin()

print(closest_to(1))
