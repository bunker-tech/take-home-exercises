# Nobel Prize Winners

## Guidelines
```
TIMEBOX:    4 hours max!
LANGUAGE:   Python
FRAMEWORKS: Any framework
TESTS:      Nice to have, but not mandatory
DOCS:       Nice to have, but not mandatory
```

# Overview
The goal of this exercise is to demonstrate your data engineering fundamentals in:
1. Data Extraction
2. Data Transformations
3. Data Modeling

The exercise consist of extracting data from the Nobel Prize API, transform, and store the data into a shape that is easy to analyze.

> :rotating_light: :exclamation: :point_right: **Please use the APIDocs here to extract your data: [Nobel Prize API](https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1#/default/get_nobelPrizes)** :point_left: :exclamation: :rotating_light:

- Create a data extractor that supports pagination, to extract all Nobel Prizes that have been won since 1901. You will only need to extract data from the **GET /NobelPrizes** endpoint, keep only the "en" values.
- Transform and store the data in tables that are in 3NF (csv is preferred since its easier for you, but if you want to spin up a local instance of sqlite/relational db, it is fine as well, just note the time limit)
- The data should be in a format that is easy for me to query (for example through SQL) for the individual that has won the most number of Nobel awards.
- Include the query string for me to query your database (be it through SQL or pandas) for the individual that has won the most number of nobel awards.
- Include instructions on how to setup the data pipeline and run it

# Submitting your exercise 
See [instructions for submitting your work](https://github.com/bunker-tech/take-home-exercises/blob/master/README.md#general-instructions)
