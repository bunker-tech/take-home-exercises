# Monolithic to Serverless Multitenancy

## Guidelines
```
TIMEBOX:    4 hours max!
LANGUAGE:   Ansible/Terraform/CloudFormation
FRAMEWORKS: Any framework
TESTS:      Nice to have, but not mandatory
DOCS:       Nice to have, but not mandatory
```

# Overview
Your team is developing a web application that is hosted on AWS. The application consists of a frontend web server and a backend API server. The application uses a PostgreSQL database hosted on RDS. The team has decided to adopt a DevOps approach to software development and deployment.

## Task
Your task is to write an infrastructure as code script that can be used to deploy the web application to AWS. However, since actual deployment to the cloud can be expensive and time-consuming, you should focus on local testing and simulation of deployment to the cloud.

You should assume that the following resources are already provisioned:

- An AWS account with appropriate permissions
- A VPC with public and private subnets
- An Internet Gateway attached to the VPC
- A NAT Gateway attached to the private subnet
- An RDS instance running PostgreSQL

Your infrastructure as code script should provision the following resources:

- An EC2 instance to run the frontend web server
- An EC2 instance to run the backend API server
- A load balancer to distribute traffic between the two instances
- An Auto Scaling group to ensure that there are always two instances running
- A security group that allows traffic from the load balancer to the instances
- A security group that allows traffic from the instances to the RDS instance

You should use the latest version of Node.js and the PostgreSQL client library to set up the frontend and backend servers. You should also configure the instances to log to CloudWatch Logs.

Your infrastructure as code script should be written in either CloudFormation/Terraform/Ansible. You should include detailed instructions on how to simulate the deployment of the infrastructure and how the deployment experience will be like.

# Submitting your exercise 
See [instructions for submitting your work](https://github.com/bunker-tech/take-home-exercises/blob/master/README.md#general-instructions)
