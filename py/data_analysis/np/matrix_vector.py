import numpy as np

sumEveryOther = np.array([[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1]])
print(sumEveryOther)

sumEveryThird = np.array([[1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1]])
print(sumEveryThird)


sumEveryThirdTile = np.tile(np.eye(3, dtype=int), 2)
print(sumEveryThirdTile)