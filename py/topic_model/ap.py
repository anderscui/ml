# coding=utf-8
from __future__ import absolute_import, unicode_literals

import matplotlib.pyplot as plt
from gensim import corpora, models

corpus = corpora.BleiCorpus('../../data/ap/ap.dat', '../../data/ap/vocab.txt')

num_topics = 100
model = models.LdaModel(corpus=corpus,
                        num_topics=num_topics,
                        id2word=corpus.id2word,
                        alpha=1.0)

doc = corpus.docbyoffset(0)
topics = model[doc]
print(topics)

num_topics_used = [len(model[doc]) for doc in corpus]
plt.hist(num_topics_used)
plt.show()
