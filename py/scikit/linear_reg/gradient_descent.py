import numpy as np

from sklearn.datasets import load_boston
from sklearn.linear_model import SGDRegressor
from sklearn.cross_validation import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split

# load and split data
data = load_boston()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)

# scale the features
X_scaler = StandardScaler()
y_scaler = StandardScaler()

X_train = X_scaler.fit_transform(X_train)
y_train = y_scaler.fit_transform(y_train)
X_test = X_scaler.fit_transform(X_test)
y_test = y_scaler.fit_transform(y_test)

# train
regressor = SGDRegressor(loss='squared_loss')
scores = cross_val_score(regressor, X_train, y_train, cv=5)
print('Cross validation r-squared scores: {0}'.format(scores))
print('Average cross validation r-squared score: {0}'.format(np.mean(scores)))

regressor.fit_transform(X_train, y_train)
print('Test set r-squared score: {0}'.format(regressor.score(X_test, y_test)))
