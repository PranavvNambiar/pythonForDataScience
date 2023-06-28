"""
Pandas is typically used for working in tabular data(similar to the data stored in spreadsheet).
Pandas provides helper functions to read data from varios file formats like CSV, Excel spreadsheets, HTML tables, JSON, SQL, and more.
"""
from urllib.request import urlretrieve as url
import os

print(os.getcwd())
url(
    "https://raw.githubusercontent.com/nlihin/data-analytics/main/datasets/italy-covid-daywise.csv",
    "./Pandas/italy-covid-daywise.csv",
)

import pandas as pd

covid_df = pd.read_csv("./Pandas/italy-covid-daywise.csv")

print(type(covid_df))

# print(covid_df)

# Data from the file is read and stored in a DataFrame object - one of the core data structures in Pandas for storing and working with tabular data.
# We typically use the .._df suffix in the variable name for the dataframes.

# *Basic information about the dataframe can be listed by using the .info() method.
# *'object' is a generic datatype when Pandas cannot figure out what datatype a column is
print(covid_df.info())

# *The .describe() method can be used on numeric columns which is used for statistical information like mean, standard deviation, minimum/maximum values and no.of non-empty values
print(covid_df.describe())

# .columns - Returns the list of columns within the data frame.
print(covid_df.columns)

# .shape - Retrieves the number of rows and columns in the data frame
print(covid_df.shape)

# Now if we want to retreive a particular element from the dataframe.
# Dataframe can be thought of dictionary of lists.
# The keys are column names and the values are lists/arrays containing data
# for the respective columns.

print(covid_df["date"][1])

""" Representing data in this format has benefits:-
1)All values in a column are typicaly have the same type of value 
    so its more efficient to store them in a single array
2)Retrieving the values for a particular row simply requires extracting the 
    elements at a given index from each of the column arrays.
3)The representation is more compact(column names are recorded only once) 
    compared to other formats where you might use a dictionary for each row of data"""

# *This is how dataframes store data
covid_data_dict = {
    "date": ["2020-08-30", "2020-08-31", "2021-09-01", "2020-09-02", "2020-09-03"],
    "new_cases": [1444, 1365, 996, 975, 1326],
    "new_deaths": [1, 4, 6, 8, 6],
    "new_tests": [53541, 42583, 54395, None, None],
}

#!Dataframes do not store data like this
covid_data_list = [
    {"date": "2020-08-30", "new_cases": 1444, "new_deaths": 1, "new_tests": 53541},
    {"date": "2020-08-31", "new_cases": 1365, "new_deaths": 4, "new_tests": 42583},
    {"date": "2021-09-01", "new_cases": 996, "new_deaths": 6, "new_tests": 54395},
    {"date": "2020-09-02", "new_cases": 975, "new_deaths": 8, "new_tests": None},
    {"date": "2020-09-03", "new_cases": 1326, "new_deaths": 6, "new_tests": None},
]

print(covid_data_dict["new_cases"])

print(covid_df["new_cases"])
# ^Each column is represented using a data structure called Series, which is usually a numpy array with some extra methods and properties.
print(type(covid_df["new_cases"]))

# //print(covid_df["new_cases"][300])
# This returns a specific row in a columns
# We first specify the row index and then its corresponding column.
print(covid_df.at[246, "new_cases"])

# Instead of using the indexing notation [], we can also access columns as properties of the data frame using the '.' notation.

print(covid_df.new_cases)  # Same as print(covid_df['new_cases])

cases_df = covid_df[["date", "new_cases"]]
print(cases_df)

# Now, cases_df is simply a 'view' of the original data frame covid_df, they point to the same data in the computers memory
# ^As they are related changing a value in one, will change the value in the other data frame which is derived from it.

# To copy values to a new variable, we use the .copy() function
covid_df_copy = covid_df.copy()
# The data in covid_df_copy is seperate from covid_df, changing values in one will not affect the other

# To access a specific row of data, we use the .loc() method
print(covid_df.loc[243])

# .head() is used to show the first n number of row in the table given that 'n' index provided
# .tail() is used to show the last n number of row in the table given that 'n' index provided
print(covid_df.head(5))
print(covid_df.tail(3))

# Whenever there is a blank value in a CSV column, there will be a "NaN" inserted.

print(covid_df.at[0, "new_tests"])
print(type(covid_df.at[0, "new_tests"]))  # The NaN's datatype will be  as a float.

# * The distinction between 0 and NaN is important
# We can find the first index that doesnt contain a 'NaN' value using 'first_valid_index' method of a series.

print(covid_df.new_tests.first_valid_index())

print(covid_df.loc[108:113])

# ^ The .sample() method is used to retrieve a random sample of rows from the data frame. This method retains the original index of data in the CSV
print(covid_df.sample(4))
