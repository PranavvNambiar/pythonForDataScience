"""
Scatter Plots
A line plot is used to represent some values in a sequence whereas,
In a scatter plot, the values of 2 variables are plotted as points on a 2D grid.
*The 'Iris flower dataset' provides samples measurements of sepals and petals for 3 species of flowers
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from urllib.request import urlretrieve as url

url(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv",
    "./Data Visualization with Matplotlib And Seaborn/iris.csv",
)
flowers_df = pd.read_csv("./Data Visualization with Matplotlib And Seaborn/iris.csv")

#!sns.load_dataset() can also be used to load the dataset without saving a local copy of the CSV, but using pandas and saving the file into the system is faster.
# flowers_df = sns.load_dataset("iris")
sns.set_style("darkgrid")
print(flowers_df)
print(flowers_df.info())
print(flowers_df.species.unique())

plt.plot(flowers_df.sepal_length, flowers_df.sepal_width)
plt.close()
# plt.show()
# This is a column from the dataframe which is a series object. This is similar to a list which can be iterated over. Lists, Numpy arrays, series, etc.all can be used to plot

# Since this plot has a 150 values, a line chart is very confusing to visualize data, so we will use scatterplot.
# sns.scatterplot().help

# //sns.scatterplot(flowers_df.sepal_length, flowers_df.sepal_width)
# In Seaborn version >= 12.0, this is the syntax for scatterplot
sns.scatterplot(data=flowers_df, x="sepal_length", y="sepal_width")
plt.close()
# plt.show()

# With the above scatterplot, we notice that all the points form a cluster, now if want to diffrentiate the different points, in this case according to the species of flower, we use 'hue'. Adding hue's makes the plot more informative.
sns.scatterplot(
    data=flowers_df, x="sepal_length", y="sepal_width", hue=flowers_df.species, s=100
)

# * Hue highlights the different kinds of points with different colors, 's' is used to denote the size of each point.
plt.close()
# plt.show()

# As seaborn builds on top of matplotlib, we can run some matplotlib.pyplot functions prior to running the seaborn functions
plt.figure(figsize=(12, 6))
plt.title("Sepal Dimensions")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
sns.scatterplot(
    data=flowers_df, x="sepal_length", y="sepal_width", hue=flowers_df.species, s=100
)
plt.close()
# plt.show()

# Seaborn has in-built support for Pandas data frames. Instead of passing each column as a series, you can also pass column names and use the data arguements to pass the data frames.
plt.title("Sepal Dimensions")
sns.scatterplot(
    data=flowers_df, x="sepal_length", y="sepal_width", hue="species", s=100
)
# plt.show()
plt.close()
