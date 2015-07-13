# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:53:04 2015

@author: andersc
"""

import matplotlib.pyplot as plt
X = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [18]]

# plt.figure()
# plt.title('Pizza price plotted against diameter')
# plt.xlabel('Diameter in inches')
# plt.ylabel('Price in dollars')
# plt.plot(X, y, 'k.')
# plt.axis([0, 25, 0, 25])
# plt.grid(True)
# plt.show()

from sklearn.linear_model import LinearRegression

# fit the model
lr = LinearRegression()
model = lr.fit(X, y)
print('A 12" pizza should cost: $%.2f' % model.predict([12])[0])

import numpy as np
print('Residual sum of squares: %.2f' % np.mean((model.predict(X) - y) ** 2))

# evaluate
X_test = [[8], [9], [11], [16], [12]]
y_test = [[11], [8.5], [15], [18], [11]]

print('R-squared: %.4f' % model.score(X_test, y_test))
