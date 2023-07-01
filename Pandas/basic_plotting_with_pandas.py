import pandas as pd
from urllib.request import urlretrieve as url
import matplotlib.pyplot as plt

result_df = pd.read_csv("./Pandas/results.csv")
print(result_df)

covid_df = pd.read_csv("./Pandas/italy-covid-daywise.csv")
covid_df["month"] = pd.DatetimeIndex(covid_df.date).month
covid_month_df = covid_df.groupby("month")[
    ["new_cases", "new_deaths", "new_tests"]
].sum()

# result_df.new_cases.plot()
# plt.show()
# This is being commented so this does not plot the graph everytime
# Important to use use this package to display the graph

# After we run this we realise that, we cannot locate the peak correctly because the values are being indexed according to the index number (which is not useful) instead of the date

# With this, the 'date' column becomes the index and the 'inplace' is used to ensure that the changes are occuring in the current dataframe and not to create a new dataframe.
# With this, the index becomes a string instead of a integer.
# * Index of a dataframe does not have to be numeric
result_df.set_index("date", inplace=True)
print(result_df)

print(result_df.loc["2020-09-01"])
print(result_df.new_cases)

# result_df.new_cases.plot()
# result_df.new_deaths.plot()
# plt.show()
# The Blue Line represents the first plot statements
# The Orange Line represents the second plot statements

# result_df.total_cases.plot()
# result_df.total_deaths.plot()
# plt.show()

death_rate = result_df.total_deaths / result_df.total_cases
# death_rate.plot(title="Death Rate")
# plt.show()

positive_rate = result_df.total_cases / result_df.total_tests
# positive_rate.plot(title="Positive Rate")
# plt.show()

covid_month_df.new_cases.plot(kind="bar")
plt.show()
covid_month_df.new_tests.plot(kind="bar")
plt.show()
