import pandas as pd

df = pd.read_csv('../../../data/winequality-red.csv', sep=';')
# print(df.describe())

import matplotlib.pylab as plt
# plt.scatter(df['alcohol'], df['quality'])
# plt.xlabel('Alcohol')
# plt.ylabel('Quality')
# plt.title('Alcohol Against Quality')
# plt.show()

# # fitting and evaluating
# from sklearn.linear_model import LinearRegression
# from sklearn.cross_validation import train_test_split
#
# X = df[list(df.columns)[:-1]]
# y = df['quality']
# X_train, X_test, y_train, y_test = train_test_split(X, y)
#
# regressor = LinearRegression()
# regressor.fit(X_train, y_train)
# # predictions = regressor.predict(X_test)
# print('R-squared: %.5f' % regressor.score(X_test, y_test))

from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import cross_val_score

X = df[list(df.columns)[:-1]]
y = df['quality']

regressor = LinearRegression()
scores = cross_val_score(regressor, X, y, cv=5)
print(scores.mean())
print(scores)
