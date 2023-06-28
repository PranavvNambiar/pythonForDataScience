import pandas as pd

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

#!Querying and Sorting Rows
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
