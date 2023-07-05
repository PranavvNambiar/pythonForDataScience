"""
Bar Charts
Bar charts are quite similar to line charts, i.e they show a sequence of values,
however a bar is shown for each value, rather tham points connected by lines. We can use the 'plt.bar()' 
function to draw a bar chart
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from urllib.request import urlretrieve as url

years = range(2000, 2006)
apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]

# plt.plot(years, apples)
plt.bar(years, apples)
# plt.show()
plt.close()

plt.bar(years, apples)
plt.plot(years, apples, "o--r")
# plt.show()
plt.close()

plt.bar(years, apples)
plt.bar(years, apples, bottom=apples)
# plt.show()
plt.close()

# Uncomment these two lines to save the CSV locally
# tips_df = sns.load_dataset("tips")
# tips_df.to_csv("./Data Visualization with Matplotlib And Seaborn/tips.csv", index=False)

# Dataset containing information about customers visiting the restaraunt through Thursday to Sunday.
tips_df = pd.read_csv("./Data Visualization with Matplotlib And Seaborn/tips.csv")
print(tips_df)
print(tips_df.info())
print(tips_df.describe())
print(type(tips_df))
print(tips_df.day.info())

# tips_df["day"] = pd.to_datetime(tips_df.day)

bill_avg_df = tips_df.groupby("day")[["total_bill"]].mean()
print(bill_avg_df)
print(bill_avg_df.index)
plt.bar(bill_avg_df.index, bill_avg_df.total_bill)
# plt.show()
plt.close()
# Doing this simple calculation takes two lines of code, so sns provides a barplot function to do the same in one line

plt.title("Restaurant Bills")
sns.barplot(x="day", y="total_bill", data=tips_df)
# The line that shows is called the confidence interval and indicates that 50% of the values lie in that range
# plt.show()
plt.close()

sns.barplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=tips_df,
    order=["Thur", "Fri", "Sat", "Sun"],
)
# plt.show()
plt.close()

sns.barplot(
    x="day",
    y="total_bill",
    hue="smoker",
    data=tips_df,
    order=["Thur", "Fri", "Sat", "Sun"],
    hue_order=["Yes", "No"],
)
# plt.show()
plt.close()

# We can also flip the bar horizontally by interchanging the x and y values
sns.barplot(
    x="total_bill",
    y="day",
    hue="smoker",
    data=tips_df,
    order=["Thur", "Fri", "Sat", "Sun"],
    hue_order=["Yes", "No"],
)
# plt.show()
plt.close()

# ? Heatmap
"""
A heatmap is used to visualize 2-dimensional data like matrix or table using colors.
"""
flights_df_main = sns.load_dataset("flights")
# flights_df_main.to_csv(
#     "./Data Visualization with Matplotlib And Seaborn/flights.csv", index=False
# )
plt.plot(flights_df_main.passengers)
# plt.show()
plt.close()

flights_df = sns.load_dataset("flights").pivot(
    index="month", columns="year", values="passengers"
)
flights_df.to_csv(
    "./Data Visualization with Matplotlib And Seaborn/flights_main.csv",
    index=False,
)
print(flights_df)
# flights_df is a matrix with one row for each month and column of each year. The values in the matrix show the number of passengers(in thousands) that visited the airport in a specific month of a specific year.

plt.title("No of Passengers (1000)")
sns.heatmap(flights_df)
# plt.show()
plt.close()
# The brighter colors indicate a higher footfall at the airport. We can infer 2 things:-
# The footfall at the airport in any given year trends to be the highest year around July & August
# The footfall at the airport in any given month tends to grow year by year

# * We can display the actual values by specifying 'annot=True' and use the 'cmap' arguement to change the color palette.

plt.title("No of Passengers (1000)")
sns.heatmap(flights_df, fmt="d", annot=True, cmap="Blues")
# plt.show()
plt.close()
