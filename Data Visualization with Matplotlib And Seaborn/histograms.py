"""
*A histogram represents the distribution of data by forming 
*bins along the range of the data and then drawing bars to show the number of observations falling into each bin 
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from urllib.request import urlretrieve as url
import numpy as np

url(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv",
    "./Data Visualization with Matplotlib And Seaborn/iris.csv",
)

flowers_df = pd.read_csv("./Data Visualization with Matplotlib And Seaborn/iris.csv")

print(flowers_df.sepal_width.sort_values(ascending=False).head(1))

# If we want to find the count, mean, max, etc kind of details in a dataframe, the run the describe() function.
print(flowers_df.describe())

sns.set_style("darkgrid")
plt.title("Distribution of Sepal Width")
plt.hist(flowers_df.sepal_width)
# With this, the sepal width is split into 10 intervals by default.
# * They are called intervals mathematically and called bins in statistics
# plt.show()
plt.close()

# Controlling the size and number of bins
plt.title("Distribution of Sepal Width")
plt.hist(flowers_df.sepal_width, bins=5)
# plt.show()
plt.close()

# ^Bins can also be controlled using the np.arange function
plt.title("Distribution of Sepal Width")
plt.hist(flowers_df.sepal_width, bins=np.arange(2, 5, 0.25))
# plt.show()
plt.close()
# We can also set unequal bins
plt.title("Distribution of Sepal Width")
plt.hist(flowers_df.sepal_width, bins=[1, 3, 4, 4.5])
# plt.show()
plt.close()

# ? Multiple Histograms
# This can be done done by reducing the opacity of each histogram, so the bars dont hide each other.

setosa_df = flowers_df[flowers_df.species == "setosa"]
versicolor_df = flowers_df[flowers_df.species == "versicolor"]
virginica_df = flowers_df[flowers_df.species == "virginica"]

plt.xlabel("Sepal Width")
plt.ylabel("Number of Flowers")
plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25))
plt.hist(versicolor_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25))
plt.legend(["Setosa", "Versicolor"])
# plt.show()
plt.close()

# * We can also stack histograms on top of each other, can be done by passing both the histograms data in a single histogram IN THE FORM OF A LIST and setting the 'stacked' attribute as True
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width")
plt.ylabel("Number of Flowers")
plt.hist(
    [
        setosa_df.sepal_width,
        versicolor_df.sepal_width,
        virginica_df.sepal_width,
    ],
    bins=np.arange(2, 5, 0.25),
    stacked=True,
)
plt.legend(["Setosa", "Versicolor", "Virginica"])
plt.show()
plt.close()
