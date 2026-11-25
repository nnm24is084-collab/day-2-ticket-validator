# Day 2 - Python Ticket Validator

## Objective
Build a typed Python package to validate AMC/service ticket CSV files.

## Technologies
- Python
- Pydantic
- Pytest
- CSV
- Logging

## Features
- Ticket data validation
- CSV file reading
- Valid and invalid row separation
- Logging of validation results
- Automated tests

## Run the project

Install dependencies:

```bash
pip install -e ".[dev]"
```

Run tests:

```bash
pytest -v
```

## Test cases
1. Valid ticket
2. Missing field
3. Invalid date
4. Invalid status
5. Empty CSV file