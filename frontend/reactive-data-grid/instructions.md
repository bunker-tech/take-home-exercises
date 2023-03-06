# Creating a reactive data grid 

## Guidelines
```
TIMEBOX:    6 hours max! (strictly, we don't want to waste your time as well)
LANGUAGE:   Typescript (no plain javascript please) 
FRAMEWORKS: ReactJS or NextJS (+ any open-source libraries that may aid you)
TESTS:      Nice to have, but not mandatory
DOCS:       Nice to have, but not mandatory
```

# Overview
John Doe wants to start understanding his spending habits better. He wants you to create a table that will allow him to better understand his finances and gain insights on where he could possibly cut down his spending. John Doe has a dataset of 10,000 transactions he wants to look through.

> :rotating_light: :exclamation: :point_right: **Please use the dataset provided here [/shared/sample_transactions.csv](/shared/sample_transactions.csv)** :point_left: :exclamation: :rotating_light:

Things the interface need to achieve: 
* Datagrid showing the full list of transactions and all their fields
  * It should be able to hold thousands of rows while maintaining a smooth and relatively lag-free experience
* Ability to sort by amount and date
* Search bar that dynamically displays a filtered list of transactions that changes depending on what the user types in it in real-time

Stretch Goals: 
* Another table that aggregates the transactions by counterparty
  * Clicking on a counterparty on this table should populate the transaction table with only the transactions by the given counterparty
* Line graph that shows spending trends over time

The main focus will be on whether you are able to meet the exercise requirements and how well you structure your code and React components. 

Wherever the requirements are ambiguous to you, feel free to clarify with us. Or exercise your discretion, but be ready to rationalise your design decisions!

Aesthetics of the datagrid is not a priority here, but you're free to flex your design skills if you want :)

# Submitting your exercise 
See [instructions for submitting your work](https://github.com/bunker-tech/take-home-exercises/blob/master/README.md#general-instructions)


