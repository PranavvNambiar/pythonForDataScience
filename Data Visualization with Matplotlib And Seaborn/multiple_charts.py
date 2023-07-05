import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from urllib.request import urlretrieve as url
from PIL import Image

sns.set_style("darkgrid")

# Matplotlib and Seaborn also support plotting multiple charts in a grid.
# It can be done using 'plt.subplots' which returns a set of axes that can be used for plotting.

plt.subplots(2, 3)  # They are the rows and columns we need
# plt.show()
plt.close()

plt.subplots(2, 3)
# As these values are overlapping a bit, we can specify the spacing between these.
plt.tight_layout(pad=2)
# plt.show()
plt.close()

fig, axes = plt.subplots(2, 3)
plt.tight_layout(pad=2)
# plt.show()
plt.close()

print(axes)
print(axes.shape)
print(axes[0, 0])
# Now we realize that each axes represents a single plot in the subplots.
# Therefore, we can plot a graph on a single axes
years = range(2000, 2012)
apples = [
    0.895,
    0.91,
    0.919,
    0.929,
    0.931,
    0.934,
    0.936,
    0.937,
    0.9375,
    0.938,
    0.937,
    0.9405,
]
oranges = [
    0.962,
    0.941,
    0.930,
    0.923,
    0.918,
    0.908,
    0.907,
    0.904,
    0.901,
    0.900,
    0.902,
    0.898,
]
flowers_df = pd.read_csv("./Data Visualization with Matplotlib And Seaborn/iris.csv")
# fig, axes = plt.subplots(2, 3)
# We can change the size of the figure by:-
fig, axes = plt.subplots(2, 3, figsize=(12, 9))
axes[0, 0].plot(years, apples, "s-b")
axes[0, 0].plot(years, oranges, "o--r")
axes[0, 0].set_title("Crop Yields in Kanto")
axes[0, 0].set_xlabel("Years")
axes[0, 0].set_ylabel("Yield (tons p/hectare)")
axes[0, 0].legend(["Apples", "Oranges"])

axes[0, 1].set_title("Sepal Length vs Width")
sns.scatterplot(
    data=flowers_df,
    x="sepal_length",
    y="sepal_width",
    hue="species",
    s=100,
    ax=axes[0, 1],
)
# ^To select which axes the scatterplot should be plotted in, seaborn provides an 'ax' attribute

setosa_df = flowers_df[flowers_df.species == "setosa"]
versicolor_df = flowers_df[flowers_df.species == "versicolor"]
virginica_df = flowers_df[flowers_df.species == "virginica"]
axes[0, 2].set_title("Distribution of Sepal Width")
axes[0, 2].hist(
    [
        setosa_df.sepal_width,
        versicolor_df.sepal_width,
        virginica_df.sepal_width,
    ],
    bins=np.arange(2, 5, 0.25),
    stacked=True,
)
axes[0, 2].legend(["Setosa", "Versicolor", "Virginica"])

tips_df = pd.read_csv("./Data Visualization with Matplotlib And Seaborn/tips.csv")
axes[1, 0].set_title("Restaurant Bills")
sns.barplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=tips_df,
    order=["Thur", "Fri", "Sat", "Sun"],
    hue_order=["Male", "Female"],
    ax=axes[1, 0],
)


flights_df = sns.load_dataset("flights").pivot(
    index="month", columns="year", values="passengers"
)
axes[1, 1].set_title("Flight Traffic")
sns.heatmap(flights_df, cmap="Blues", ax=axes[1, 1])

img = Image.open("./Data Visualization with Matplotlib And Seaborn/chart.jpg")
axes[1, 2].set_title("Data Science Meme")
axes[1, 2].imshow(img)
axes[1, 2].grid(False)
axes[1, 2].set_xticks([])
axes[1, 2].set_yticks([])

plt.tight_layout(pad=2)
plt.show()
plt.close()
