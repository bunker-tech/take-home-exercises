# [TITLE OF QUESTION]

## Guidelines
```
TIMEBOX:    4 hours max! (strictly, we don't want to waste your time as well)
LANGUAGE:   Typescript (no plain javascript please), Python
FRAMEWORKS: Express/Fastify/Nest.js, FastAPI/Django/Flask
TESTS:      Nice to have, but not mandatory
DOCS:       Nice to have, but not mandatory
```

# Overview
The goal of this exercise is to design a read-only API (REST) that returns one or more records from a static set of transaction data.

> :rotating_light: :exclamation: :point_right: **Please use the dataset provided here [/shared/sample_transactions.csv](/shared/sample_transactions.csv)** :point_left: :exclamation: :rotating_light:

Requirements: 
* list transaction data via API `GET` Request
    * Filter by one or more fields/attributes (e.g. /transactions?tags=Dining,Travel&counterparty=Google)
    * Sort by one or more fields/attributes (e.g. /transactions?sort=counterparty)
* Fetch a single record via `GET` request
    * Stretch goal: return a sparse fieldset, (e.g. /transactions/32?fields=amount,tags)

* Have the JSON Response be normalized into a uniform schema via a serializer or json template
* Create OAS (OpenAPI Specification) that will allow the developer to better understand the API

Don't worry about any webapp concerns other than returning a JSON object via a GET request.
The examples above are not a contract. Feel free to design the URL structure and JSON schema which you believe will create the best developer experience.

This is an evaluation of your ability to craft a solution that meets the requirements while demonstrating craftsmanship, thoughtfulness and good architectural design decisions. 

It is not a test of how well you know your frameworks (Django/Express/Flask/Nestjs). Build something that is useful and intuitive for the user, and easy to debug/test/extend for the developer. 

# Submitting your exercise 

See [instructions for submitting your work](https://github.com/bunker-tech/take-home-exercises/blob/master/README.md#general-instructions)
