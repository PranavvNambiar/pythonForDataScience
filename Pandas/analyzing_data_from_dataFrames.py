import pandas as pd
from urllib.request import urlretrieve as url

covid_df = pd.read_csv("./Pandas/italy-covid-daywise.csv")
print(covid_df)

# The total number of reported cases and deaths related to Covid-19 in Italy
total_cases = int(covid_df.new_cases.sum())
total_deaths = int(covid_df.new_deaths.sum())
print(total_cases)
print(total_deaths)

print(
    "The total number of reported cases is {} and deaths is {} related to Covid-19 in Italy".format(
        (total_cases), (total_deaths)
    )
)

# What is the overall death ratio/rate
death_rate = total_deaths / total_cases
print("The overall death rate is {:.2f}%".format(death_rate * 100))

# What is the overall number of tests conducted? A total of 935310 tests were conducted before daily test numbers were being reported.
initial_tests = 935_310
new_tests_index = covid_df.new_tests.first_valid_index()
new_tests = covid_df.new_tests[new_tests_index:].sum()
print(new_tests)
total_tests = initial_tests + new_tests
print(total_tests)

# What fraction of tests returned a positive result
positive_rate = total_cases / total_tests
print("The overall positivity rate is {:.2f}%".format(positive_rate * 100))

# ?Querying and Sorting Rows
high_new_cases = covid_df.new_cases > 1000
print(high_new_cases)

# In this case, it will only show those rows in covid_df whose high_new_cases criteria(new_cases > 1000) is satisfied i.e which are True
print(covid_df[high_new_cases])

# Can also be done in a single line by:-
high_cases_df = covid_df[covid_df.new_cases > 1000]
print(high_cases_df)

"""
To view all the  rows in the terminal, run:
from IPython.display import display
with pd.option_context('display.max_rows', 100):
    display(covid_df[covid_df.new_cases > 1000])
"""

high_ratio_df = covid_df[(covid_df.new_cases / covid_df.new_tests) > positive_rate]
print(high_ratio_df)

covid_df["positive_rate"] = covid_df.new_cases / covid_df.new_tests

print(covid_df)

# To remove the "positive_rate" column from the dataframe
covid_df.drop(columns=["positive_rate"], inplace=True)

print(covid_df)

# ? Querying and Sorting Rows
# Will give us the first 10 values in descending order of new_cases (from most cases to least cases)
print(covid_df.sort_values("new_cases", ascending=False).head(10))
print(covid_df.sort_values("new_deaths", ascending=False).head(10))
print(covid_df.sort_values("new_cases").head(10))
"""The data at index 172 is incorrect data.
We can either:- 
1)Replace it with 0
2)Replace it with the average of the entire column
3)Replace it with the average of the values on the previous and next date
4)Discard the row entirely

The method we pick to deal with the data entirely depends on the data. In this case, as the data is in time series format, its reasonable to use the 3rd method
which is average of the previous and the next value
"""
covid_df.at[172, "new_cases"] = (
    covid_df.at[171, "new_cases"] + covid_df.at[173, "new_cases"]
) / 2

print(covid_df.at[172, "new_cases"])
print(covid_df.loc[165:175])

# ? Working with dates
print(covid_df.date)
# This datatype is currently an object, so Pandas does not know that this column is a date. We can convert it into a 'datetime' colummn.
# This can be done with the the pandas function, to_datetime() and by passing the series as a parameter
covid_df["date"] = pd.to_datetime(covid_df.date)
print(covid_df.date)

covid_df["year"] = pd.DatetimeIndex(covid_df.date).year
# The month go from 1 through 12
covid_df["month"] = pd.DatetimeIndex(covid_df.date).month
# The days go from 1 through 31,30 or 28, depending on month
covid_df["day"] = pd.DatetimeIndex(covid_df.date).day
# Weekday represents the day of the week. Monday is 0, Sunday is 6.
covid_df["weekday"] = pd.DatetimeIndex(covid_df.date).weekday

print(covid_df)

# Now if we want to aggregate the data for the month of May.
# Query the rows for May
covid_df_may = covid_df[covid_df.month == 5]
print(covid_df_may)

# But now, if we want to aggregate the data, we do not want to sum up all the columns, like year, day and weekday as their sum has no use to us, so we only take the values that are useful to us.
covid_df_may_metrics = covid_df_may[["new_cases", "new_deaths", "new_tests"]]
print(covid_df_may_metrics)

# Get the column-wise sum
covid_may_totals = covid_df_may_metrics.sum()
print(covid_may_totals)
print(type(covid_may_totals))

# This can also be done in a single line by:-
print(covid_df[covid_df.month == 5][["new_cases", "new_deaths", "new_tests"]].sum())

# Overall Average
print(covid_df.new_cases.mean())

# Average for Sundays
print(covid_df[covid_df.weekday == 6].new_cases.mean())

# ?Grouping and Aggregation
monthly_groups = covid_df.groupby("month")
# This by itself will not help us that much and aggregtion will not be performed yet.
print(monthly_groups[["new_cases", "new_deaths", "new_tests"]])
# Aggregated Data as per monthly basis
print(monthly_groups[["new_cases", "new_deaths", "new_tests"]].sum())

# Can be done in one line by:-
covid_month_df = covid_df.groupby("month")[
    ["new_cases", "new_deaths", "new_tests"]
].sum()

print(covid_df.groupby("weekday")[["new_cases", "new_deaths", "new_tests"]].mean())
# Aggregation can be done in many ways, it can be done by counts, mean, sum, etc

# Apart from grouping, another form of aggregation to calculate the running or cummulative sum of cases, test, death up to the current date for each row. This can be done by using 'cumsum' method
covid_df["total_cases"] = covid_df.new_cases.cumsum()
covid_df["total_deaths"] = covid_df.new_deaths.cumsum()
covid_df["total_tests"] = covid_df.new_tests.cumsum() + initial_tests
# We add initial test as in the start some data was not added.

# We will notice that the 'NaN' and 'total_tests' columns dont change
# If we add with a 'NaN' value, the cummulative result will also be NaN


# ^This is to display the whole table in the terminal
# with pd.option_context(
#     "display.max_rows",
#     None,
#     "display.max_columns",
#     None,
#     "display.precision",
#     3,
# ):
#     print(covid_df)
print(covid_df)

# ?Merging data from multiple sources
url(
    "https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv",
    "./Pandas/locations.csv",
)

locations_df = pd.read_csv("./Pandas/locations.csv")
print(locations_df)
print(locations_df[locations_df.location == "Italy"])

covid_df["location"] = "Italy"
print(covid_df)

#! To merge data of 2 sources like CSV's we need to have ATLEAST ONE COMMON column between them
# In this case, the common column is 'location'

# ^In this we, we want to get information out from locations dataframe and we want to get the information out using the location column.
merged_df = covid_df.merge(locations_df, on="location")
print(merged_df)

merged_df["cases_per_million"] = merged_df.total_cases * 1e6 / merged_df.population
merged_df["deaths_per_million"] = merged_df.total_deaths * 1e6 / merged_df.population
merged_df["tests_per_million"] = merged_df.total_tests * 1e6 / merged_df.population

print(merged_df)

# Saving all the useful columns of data into a csv file
result_df = merged_df[
    [
        "date",
        "new_cases",
        "total_cases",
        "new_deaths",
        "total_deaths",
        "new_tests",
        "total_tests",
        "cases_per_million",
        "deaths_per_million",
        "tests_per_million",
    ]
]
result_df.to_csv("./Pandas/results.csv", index=None)
# Using the to_csv function to save the dataframe locally, im saving it in the Pandas folder.
# If the file already exists, this overwrites the file.
# The to_csv function already includes an additional column for storing the index of the dataframe by default.
# So instead of creating a redundant index column, we can set its value to None or False, like so index=None / index=False
