import pandas as pd
from urllib.request import urlretrieve as url

url(
    "https://gist.githubusercontent.com/aakashns/28b2e504b3350afd9bdb157893f9725c/raw/994b65665757f4f8887db1c85986a897abb23d84/countries.csv",
    "./Pandas/countries.csv",
)

countries_df = pd.read_csv("./Pandas/countries.csv")
print(countries_df)

# Q1: How many countries does the dataframe contain?
# print(len(countries_df.index))
num_countries = countries_df.shape[0]
print("There are {} countries in the dataset\n".format(num_countries))

# Q2: Retrieve a list of continents from the dataframe?
continets_name = countries_df.continent.unique()
continents = len(countries_df.continent.unique())
print("The countries of the dataset are: ", end="")
print(*continets_name, sep=",")
print("There are {} continents in the dataset\n".format(continents))

# Q3: What is the total population of all the countries listed in this dataset?
total_population = countries_df.population.sum()
print("The total population is {}.".format(int(total_population)))

# Q: (Optional) What is the overall life expectancy across in the world?
weighted_expectancy = countries_df.population * countries_df.life_expectancy
weight_sum = weighted_expectancy.sum()
print(weight_sum)
overall_life_exp = weight_sum / total_population
print(
    "The overall life expectancy across the world is {} years of age.".format(
        int(overall_life_exp)
    )
)

# Q4: Create a dataframe containing 10 countries with the highest population.
most_populous_df = countries_df.sort_values("population", ascending=False).head(10)[
    "location"
]
print(most_populous_df)

# Q5: Add a new column in countries_df to record the overall GDP per country (product of population & per capita GDP).
countries_df["gdp"] = countries_df.population * countries_df.gdp_per_capita
print(countries_df["gdp"])

# Q: (Optional) Create a dataframe containing 10 countries with the lowest GDP per capita, among the countries with population greater than 100 million.
gdp_df = (
    countries_df[countries_df["population"] > 100e6]
    .sort_values("gdp_per_capita", ascending=True)
    .head(10)["location"]
)
print(gdp_df)

# Q6: Create a data frame that counts the number countries in each continent
country_counts_df = countries_df.groupby("continent")["location"].count()
print(country_counts_df)

# Q: Create a data frame showing the total population of each continent.
continent_populations_df = countries_df.groupby("continent")["population"].sum()
print(continent_populations_df)

# Let's download another CSV file containing overall Covid-19 stats for various countires, and read the data into another Pandas data frame.
url(
    "https://gist.githubusercontent.com/aakashns/b2a968a6cfd9fbbb0ff3d6bd0f26262b/raw/b115ed1dfa17f10fc88bf966236cd4d9032f1df8/covid-countries-data.csv",
    "./Pandas/covid-countries-data.csv",
)
covid_data_df = pd.read_csv("./Pandas/covid-countries-data.csv")
print(covid_data_df)

# Q8: Count the number of countries for which the total_tests data is missing.
total_tests_missing = pd.isna(covid_data_df["total_tests"]).sum()
print(
    "The data for total tests is missing for {} countries.".format(
        int(total_tests_missing)
    )
)

# Q9: Merge countries_df with covid_data_df on the location column.
combined_df = countries_df.merge(covid_data_df, on="location")
print(combined_df)

# **Q10: Add columns `tests_per_million`, `cases_per_million` and `deaths_per_million` into `combined_df`.**
combined_df["tests_per_million"] = (
    combined_df["total_tests"] * 1e6 / combined_df["population"]
)
combined_df["cases_per_million"] = (
    combined_df["total_cases"] * 1e6 / combined_df["population"]
)
combined_df["deaths_per_million"] = (
    combined_df["total_deaths"] * 1e6 / combined_df["population"]
)
print(combined_df)

# **Q11: Create a dataframe with 10 countires that have highest number of tests per million people.**
highest_tests_df = combined_df.sort_values("tests_per_million", ascending=False).head(
    10
)["location"]
print(highest_tests_df)

# **Q12: Create a dataframe with 10 countires that have highest number of positive cases per million people.**
highest_cases_df = combined_df.sort_values("cases_per_million", ascending=False).head(
    10
)["location"]
print(highest_cases_df)

# **Q13: Create a dataframe with 10 countires that have highest number of deaths cases per million people?**
highest_deaths_df = combined_df.sort_values("deaths_per_million", ascending=False).head(
    10
)["location"]
print(highest_deaths_df)

# **(Optional) Q: Count number of countries that feature in both the lists of "highest number of tests per million" and "highest number of cases per million".**
in_both = highest_tests_df.isin(highest_cases_df)
print(in_both)
print(
    in_both.sum(),
    'countries that feature in both the lists of "highest number of tests per million" and "highest number of cases per million"',
)

"""
!In this question, if in the highest_cases_df,highest_tests_df or highest_deaths_df if we pass only the 'location' attribute in the dataframe to be displayed. Then when we use the isin() function we dont need to pass the 'location' attribute in the in_both dataframe.
#So if we dont pass the location attribute, then to check whether the location attributes are matched in the in_both dataframe, we need to pass the location attribute.
"""

# **(Optional) Q: Count number of countries that feature in both the lists "20 countries with lowest GDP per capita" and "20 countries with the lowest number of hospital beds per thousand population". Only consider countries with a population higher than 10 million while creating the list.**
lowest_gdp_per_capita = (
    combined_df[combined_df["population"] > 10e6]
    .sort_values("gdp_per_capita", ascending=True)
    .head(20)
)
lowest_hospital_beds = (
    combined_df[combined_df["population"] > 10e6]
    .sort_values("hospital_beds_per_thousand", ascending=True)
    .head(20)
)
in_both_2 = lowest_gdp_per_capita["location"].isin(lowest_hospital_beds["location"])
print(
    in_both_2.sum(),
    'countries that feature in both the lists "20 countries with lowest GDP per capita" and "20 countries with the lowest number of hospital beds per thousand population"',
)
