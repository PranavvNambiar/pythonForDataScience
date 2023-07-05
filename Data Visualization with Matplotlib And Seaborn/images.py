import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from urllib.request import urlretrieve as url

url(
    "https://i.imgur.com/SkPbq.jpg",
    "./Data Visualization with Matplotlib And Seaborn/chart.jpg",
)
sns.set_style("darkgrid")
# Before an Image can be displayed, it has to be read into memory using the PIL module
from PIL import Image

img = Image.open("./Data Visualization with Matplotlib And Seaborn/chart.jpg")
print(type(img))
# An image loaded using PIL is simply a 3D numpy array containing pixel intensities for the red,green & blue channels of the image. We can convert the image back into an array using np.array
img_array = np.array(img)
print(img_array)
print(img_array.shape)

plt.imshow(img)
# plt.show()
plt.close()

# img.show()
# This will display the image using the computers default image displaying app(eg-gallery)

plt.grid(False)
plt.title("A Data Science Meme")
plt.axis("off")
plt.imshow(img)
# plt.show()
plt.close()

# We can also display only certain parts of the image by specifying the arrays within the image
plt.grid(False)
plt.title("A Data Science Meme")
plt.axis("off")
plt.imshow(img_array[125:325, 105:305])
plt.show()
plt.close()
