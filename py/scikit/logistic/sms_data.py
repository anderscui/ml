import pandas as pd

df = pd.read_csv('../../data/SMSSpamCollection', delimiter='\t', header=None)
print(df.head())
print('Number of spam msgs: {0}'.format(df[df[0] == 'spam'][0].count()))  # 747
print('Number of ham msgs: {0}'.format(df[df[0] == 'ham'][0].count()))  # 4825

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.cross_validation import train_test_split

X_train_raw, X_test_raw, y_train, y_test = train_test_split(df[1], df[0])
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train_raw)
X_test = vectorizer.transform(X_test_raw)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)
predictions = classifier.predict(X_test)
for i, pred in enumerate(predictions[:20]):
    print('Prediction: {0}, Message: {1}'.format(pred, X_test_raw[i]))
