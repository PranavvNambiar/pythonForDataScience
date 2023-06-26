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
