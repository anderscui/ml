import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.utils import shuffle

import mahotas as mh

# read and flatten the image
original_img = np.array(mh.imread('cat.jpg'), dtype=np.float64) / 255
original_dim = tuple(original_img.shape)
width, height, depth = tuple(original_img.shape)
image_flattened = np.reshape(original_img, (width * height, depth))

# select 1000 colors randomly
image_array_sample = shuffle(image_flattened, random_state=0)[:1000]
estimator = KMeans(n_clusters=64, random_state=0)
estimator.fit(image_array_sample)

# predict cluster assignment for each of the pixels in the original image
cluster_assignments = estimator.predict(image_flattened)

# create the compressed image from the compressed palette and cluster assignments
compressed_palette = estimator.cluster_centers_
compressed_img = np.zeros((width, height, compressed_palette.shape[1]))

label_idx = 0
for i in range(width):
    for j in range(height):
        compressed_img[i][j] = compressed_palette[cluster_assignments[label_idx]]
        label_idx += 1

plt.subplot(121)
plt.title('Original')
plt.imshow(original_img)
plt.axis('off')
plt.subplot(122)
plt.title('Compressed')
plt.imshow(compressed_img)
plt.axis('off')
plt.show()