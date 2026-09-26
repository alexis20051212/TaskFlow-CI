# TaskFlow CI

TaskFlow CI is a simple web application for managing tasks.

## Objective

The purpose of this project is to practice Git version control
and Continuous Integration using GitHub Actions.

## Technologies

- Python
- Flask
- HTML and CSS
- Git and GitHub
- pytest
- GitHub Actions

## Features

- Display a list of tasks.
- Add new tasks.
- Validate empty tasks.

## Installation

1. Clone the repository.
2. Create a virtual environment.
3. Install the dependencies.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run the application

```bash
python run.py
```

Open http://127.0.0.1:5000 in your browser.

## Run tests

```bash
python -m pytest -v
```

## Continuous Integration

GitHub Actions automatically installs the dependencies
and runs the tests when changes are pushed to the repository.
