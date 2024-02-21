# Activity 3

## Submitted By:
- Name: Harkirat Singh
- Student ID: 100447226
- E-mail-harkirat-singh6@myseneca.ca

Installation Steps

    Clone the Repository

    bash

git clone https://github.com/Harkirat19/BTP405_Lab3
cd directory-name

Build and Launch with Docker Compose

Utilize Docker Compose to build and initiate the application and database services:

bash

docker-compose up --build

This command generates the API server image and starts the services defined in docker-compose.yml.

Stop the Services

To halt the services and delete the containers, utilize the following command:

bash

docker-compose down