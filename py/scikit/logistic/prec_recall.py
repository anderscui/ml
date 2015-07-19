import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.cross_validation import train_test_split, cross_val_score

df = pd.read_csv('../../data/sms.csv')

X_train_raw, X_test_raw, y_train, y_test = train_test_split(df['message'], df['label'])
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train_raw)
X_test = vectorizer.transform(X_test_raw)
classifier = LogisticRegression()
# classifier.fit(X_train, y_train)

precisions = cross_val_score(classifier, X_train, y_train, cv=5, scoring='precision')
print('Precision: {0} - {1}'.format(np.mean(precisions), precisions))

recalls = cross_val_score(classifier, X_train, y_train, cv=5, scoring='recall')
print('Recall: {0} - {1}'.format(np.mean(recalls), recalls))

# Precision: 0.991963015647 - [ 0.97297297  1.          1.          0.98684211  1.        ]
# Recall: 0.667764127764 - [ 0.64864865  0.75675676  0.64864865  0.67567568  0.60909091]
