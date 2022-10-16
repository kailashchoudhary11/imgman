# imgman

imgman is an image manipulation website built with which provides options for converting an image to blur, black and white, grayscale, pdf.

# Table Of Content
- [imgman](#imgman)
- [Table Of Content](#table-of-content)
  - [Screenshots](#screenshots)
  - [Background](#background)
  - [Architecture](#architecture)
  - [Project Folder Structure](#project-folder-structure)
  - [Objectives](#objectives)
  - [Technologies Used](#technologies-used)
  - [imgman Features](#imgman-features)
  - [Key features and release dates](#key-features-and-release-dates)
  - [Project Status](#project-status)
  - [Running Locally](#running-locally)
    - [Prerequisites](#prerequisites)
    - [Clone the repo](#clone-the-repo)
    - [Install the requirements](#install-the-requirements)
    - [Setup Database and make migrations](#setup-database-and-make-migrations)
  - [**Making Contribution**](#making-contribution)
  - [License](#license)
  - [Code of Conduct](#code-of-conduct)
  - [Happy Coding](#happy-coding)

## Screenshots

![Screenshot (1)]

![Screenshot (2)]

![Screenshot (3)]

## Background

This project, ***imgman***, is a project initiative founded by <https://github.com/kailashchoudhary11>. It is a platform that allows users to manipulate images.

## Architecture

- Django
- img2pdf
- Pillow
- sqlite3
- OpenCV

## Project Folder Structure

```imgman
├── imgman
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── sinimg
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-38.pyc
│   │       └── __init__.cpython-38.pyc
│   ├── templates
│   │   ├── sinimg
│   │   │   ├── process.html
│   │   │   ├── select_choice.html
│   │   │   └── upload.html
│   ├── forms.py
│   ├── models.py
│   ├── helpers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates
│   ├── base.html
│   └── index.html
├── .gitignore
├── code_of_conduct.md
├── CONTRIBUTING.md
├── LICENSE
├── manage.py
├── README.md
└── requirements.txt
```

## Objectives

- [x] Create a website that allows users to manipulate images
- [ ] finish the homepage
- [ ] finish the readme
- [ ] other objectives

## Technologies Used

- HTML/CSS/Javascript (Frontend)
- Django - Framework, Python(Backend)
- GIT (Version Control)
- sqlite3 (Database)

## imgman Features

- [x] Upload an image
- [ ] choose a filter
- [ ] export the image
- [ ] integrate with other image manipulation libraries

## Key features and release dates

> Landing page
> Upload Page
> User Dashboard

## Project Status

> Project is : Development

## Running Locally

### Prerequisites

- Atleast Python 3.8
- Vscode or any other IDE
- Django 3.1.7

### Clone the repo

```bash
git clone https://github.com/kailashchoudhary11/imgman.git
```

cd imgman

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

## **Making Contribution**

- Fork the repo
- Create a new branch
- Make your changes
- Describe your changes in the pull request
- Make a pull request
- Wait for your pull request to be merged
- rockenroll

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
<https://github.com/kailashchoudhary11/imgman/blob/master/LICENSE.md>

## Code of Conduct

<https://github.com/kailashchoudhary11/imgman/blob/master/CODE_OF_CONDUCT.md>

## Happy Coding

