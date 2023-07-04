import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

# %matplotlib inline
# This command is to ensure that plots are shown and embedded into the Jupyter notebook itself

"""Types of charts
1) Line Charts
- Line Charts are one of the simplest and widely used data visualization techniques. A line chart displays information as a series of data points or markers, connected by straight lines. You can customize the shape, size, color and othe aesthetic elements of the markers and lines for better visual calrity.
"""
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
plt.plot(yield_apples)
plt.close()
# plt.show()

# In Jupyter notebooks, if we do not want to see the list of plots, etc( output information ).We add a semi-colon(;) after the plot statement

#! Customizing the X-Axis
years = [2010, 2011, 2012, 2013, 2014, 2015]
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
plt.plot(years, yield_apples)
plt.close()
# plt.show()

# Axis Labels
# We can add labels to the axes to show what ech axis represents using plt.xlabel & plt.ylabel methods
plt.plot(years, yield_apples)
plt.xlabel("Years")
plt.ylabel("Yield(tons p/hectare)")
plt.close()
# plt.show()

# Plotting Multiple Lines
# We just call plt.plot multiple times to show multiple lines on the same graph.
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
plt.plot(years, apples)
plt.plot(years, oranges)
plt.xlabel("Years")
plt.ylabel("Yield(tons p/hectare)")
plt.close()
# plt.show()

# Chart Title & Legend
# To diffrentiate between multiple lines, we can include a legend within the graph using the plt.legend() function.
# We can also give the entire chart a title using the plt.title function.
plt.plot(years, apples)
plt.plot(years, oranges)
plt.xlabel("Years")
plt.ylabel("Yield(tons p/hectare)")
plt.title("Crop Yields in Kanto")
plt.legend(["Apples", "Oranges"])
plt.close()
# plt.show()

# Line Markers
# We can also show markers for the data points on each line using the marker arguement of plt.plot. We can use markers like 'circle', 'cross', 'square','diamond', etc.
plt.plot(years, apples, marker="o")
plt.plot(years, oranges, marker="x")
plt.xlabel("Years")
plt.ylabel("Yield(tons p/hectare)")
plt.title("Crop Yields in Kanto")
plt.legend(["Apples", "Oranges"])
plt.close()
# plt.show()

plt.plot(years, apples, marker="s", c="b", ls="-", lw=2, ms=8, mew=2, mec="navy")
plt.plot(years, oranges, marker="o", c="r", ls="--", lw=3, ms=10, alpha=0.5)
plt.xlabel("Years")
plt.ylabel("Yield(tons p/hectare)")
plt.title("Crop Yields in Kanto")
plt.legend(["Apples", "Oranges"])
plt.close()
# plt.show()

# The 'fmt' arguement provides shorthand for specifying the line style, marker and line color. It can be provided as the third arguement to plt.plot
# fmt - '[marker][line][color]'
plt.plot(years, apples, "s-b")
plt.plot(years, oranges, "o--r")
plt.xlabel("Years")
plt.ylabel("Yield(tons p/hectare)")
plt.title("Crop Yields in Kanto")
plt.legend(["Apples", "Oranges"])
plt.close()
# plt.show()

# If no line style is mentioned, only markers are drawn.
plt.plot(years, oranges, "or")
plt.title("Yield of Oranges(tons p/hectare)")
plt.close()
# plt.show()

# Changing the figure size
# You can use the plt.figure function to change the size of the figure.
plt.figure(figsize=(12, 6))
plt.plot(years, oranges, "or")
plt.title("Yield of Oranges(tons p/hectare)")
plt.close()
# plt.show()

# We can style our charts by using the 'Seaborn' library
# Some styles like this can be applied to all plots.

# sns.set_style("whitegrid")
plt.plot(years, apples, "s-b")
plt.plot(years, oranges, "o--r")
plt.xlabel("Years")
plt.ylabel("Yield(tons p/hectare)")
plt.title("Crop Yields in Kanto")
plt.legend(["Apples", "Oranges"])
plt.close()
# plt.show()

# *Important thing to remember is if we call set_style in seaborn once, every subsequent plot will also have the same set_style
sns.set_style("darkgrid")
plt.plot(years, apples, "s-")
plt.plot(years, oranges, "o--")
plt.xlabel("Years")
plt.ylabel("Yield(tons p/hectare)")
plt.title("Crop Yields in Kanto")
plt.legend(["Apples", "Oranges"])
# plt.close()
plt.show()

# If we want to change the parameters in matplotlib themselves, then we run:-
# matplotlib.rcParams['font.size'] = 14
# matplotlib.rcParams['figure.figsize'] = (9,5)
# matplotlib.rcParams['figure.facecolor'] = '#00000000'
