# demo_spring_api

A simple Spring Boot REST API.

## Description

The API provides a simple CRUD interface for a `Product` entity. The entity has the following fields:

- `id` (Long)
- `name` (String)
- `price` (Double)

The API provides the following endpoints:

- `GET /product`: Get all products
- `GET /product/{id}`: Get a product by ID
- `POST /product`: Create a new product (requires a JSON body with the product fields: `name` and `price`)
- `PUT /product`: Update a product by ID (requires a JSON body with the product fields: `id`, `name` and `price`)
- `DELETE /product/{id}`: Delete a product by ID

## How to run

Using Docker:

Since the API relies on a database, it is easier to run it using Docker. The `docker-compose.yml` file in the root directory of the project defines a service for the API and a service for the database. To run the stack, execute the following command in the root directory of the project:

```shell

    docker compose up

```

The API will be available at `http://localhost:8080`.

## How to build

To build the project, execute the following command in the root directory of the project:

```shell

    mvn clean package

```

The command will generate a JAR file in the `target` directory of the project. The JAR file can be run using the following command:

```shell

    java -jar target/demo_spring_api-0.0.1-SNAPSHOT.jar

```

or 

```shell

    mvn spring-boot:run

```

## Testing using JMeter

The `JMeter Data` contains sample data for testing the API using JMeter. The python script `generate_data.py` can be used to generate a CSV file with random data. The script requires the `Faker` library. To install the library, execute the following command:

```shell

    pip install Faker

```

To generate the CSV file, execute the following command:

```shell

    python generate_data.py

```

The script will also create test data for the database. The CSV files can be used in JMeter to test the API.

You can use [OpenAPI Generator CLI](https://openapi-generator.tech/docs/installation/) to generate the JMeter test plan.
