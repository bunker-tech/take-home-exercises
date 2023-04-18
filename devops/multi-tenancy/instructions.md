# Monolithic to Serverless Multitenancy

## Guidelines
```
TIMEBOX:    4 hours max!
LANGUAGE:   Any language
FRAMEWORKS: Any framework
TESTS:      Nice to have, but not mandatory
DOCS:       Nice to have, but not mandatory
```

# Overview
You are working as a DevOps Engineer for a software development company that builds a web application for managing customer data. The application runs on a monolithic architecture, vertically scaled on EC2. The company wants to implement a multitenancy architecture and ensure a smooth CI/CD pipeline, using a serverless framework.

## Task
Your task is to design a whitepaper that outlines a roadmap to implement a new feature that allows customers to manage their data across multiple regions. You also need to design and outline a multitenancy architecture for the microservices. 

The focus on the design should be ease of development, security, and cost savings. Go into the technologies you plan to use and the design choices that you plan to execute.

Key areas to focus on:
- Data isolation between tenants
- Authentication and authorization for services
- CI/CD
- Observability

## Requirements
- The CI/CD pipeline should be implemented using a CI/CD tool of your choice.
- The pipeline should include stages for building, testing, and deploying the application.
- The application should be deployed on a serverless architecture.
- The multitenancy architecture should allow multiple customers to access the application, with their data and settings isolated from each other.
- The architecture should also support different regions, with each customer able to access their data from any region.

## Deliverables
- A whitepaper outlining the roadmap to implement the new feature and the multitenancy architecture for the microservices.

## Assumptions
- You have access to a serverless platform such as AWS Lambda or Azure Functions.
- The application has already been deployed on the platform.