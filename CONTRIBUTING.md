# Contributing Guidelines

Before contributing, please read through the guidelines carefully.

## installation and Usage

### Prerequisites

- Atleast Python 3.8
- Vscode or any other IDE
- Django 3.1.7

### Clone the repo

```bash
git clone https://github.com/kailashchoudhary11/imgman.git
```

### ***Create New Virtual Environment***

1. Cd into Project Directory
2. Open New Terminal and Run

```bash
py -m venv venv
```

1. Activate Virtual Env

```bash
.\env\Scripts\activate
```

[Virtual Environment setup guide](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)

***note: you should be on the same dir as requirements.txt file***

### Install the requirements

```bash
pip install -r requirements.txt
```

### Setup Database and make migrations

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

## Pull Requests
We actively welcome your pull requests.

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.


## Issues
We use GitHub issues to track public bugs. Please ensure your description is
clear and has sufficient instructions to be able to reproduce the issue.

## License
By contributing to imgman, you agree that your contributions will be licensed under the LICENSE file in
the root directory of this source tree.
