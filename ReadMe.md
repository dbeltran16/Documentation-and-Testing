# Flask API Documentation and Testing

## Overview

This workspace currently contains a Flask application entrypoint with in-memory sample data and a set of unit tests built with Python's `unittest` framework.

The goal is to keep the current code easy to run, easy to test, and easy to extend.

## Setup

From a terminal, change into this project folder first:

```bash
cd "c:\Users\darle\.vscode\my-first-site\Back End M2\Documentation and Testing\my_flask_api"
```

Then install dependencies from the project root:

```bash
pip install -r requirements.txt
```

## Current Project Structure

```text
my_flask_api/
├── tests/
│   ├── __init__.py
│   ├── test_customers.py
│   ├── test_mechanics.py
│   └── test_services.py
├── requirements.txt
├── run.py
├── swagger.py
└── ReadMe.md
```

## What Is Implemented Now

The current application entrypoint in [run.py](run.py) exposes these routes:

- `GET /`
- `GET /customers`
- `GET /customers/<customer_id>`
- `PUT /customers/<customer_id>`
- `GET /mechanics`
- `GET /services`

HTTP request method:

- `GET`
- `PUT`

In-memory sample data included now:

- 4 customers
- 3 mechanics
- 3 services

Behavior:

- Returns `200 OK` on `GET /` with a JSON status message
- Returns `200 OK` for existing customers, mechanics, and services
- Returns `200 OK` when an existing customer is updated with a valid `name`
- Returns `400 Bad Request` when `name` is missing
- Returns `404 Not Found` when the customer ID does not exist

## Test Coverage

The current test files define in-test Flask apps and cover these cases:

HTTP request methods used in the tests:

- `GET`
- `POST`
- `PUT`
- `DELETE`

- [tests/test_customers.py](tests/test_customers.py)
	- `GET /customers` returns `200 OK` and 4 customers
	- `POST /customers` returns `201 Created` when `name` is present
	- `PUT /customers/1` returns `200 OK`
	- `DELETE /customers/1` returns `200 OK`
	- `POST /customers` returns `400 Bad Request` when `name` is missing
	- `GET /customers/9999` returns `404 Not Found`
- [tests/test_mechanics.py](tests/test_mechanics.py)
	- `GET /mechanics` returns `200 OK` and 3 mechanics
	- `GET /mechanics/9999` returns `404 Not Found`
- [tests/test_services.py](tests/test_services.py)
	- `GET /services` returns `200 OK` and 3 services
	- `GET /services/9999` returns `404 Not Found`

The current tests are self-contained Flask apps that verify both positive and negative responses for the customer, mechanic, and service routes.

## Running the Application

Start the Flask application by running:

```bash
python run.py
```

## Running the Tests

Run every test in the project with the following command.

Windows:

```bash
python -m unittest discover tests
```

macOS/Linux:

```bash
python3 -m unittest discover tests
```

If all tests pass, the current workspace behavior is working as expected.
