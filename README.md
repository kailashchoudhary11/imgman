# imgman

imgman is an image manipulation website built with django, which provides options for converting an image to blur, black and white, grayscale, pdf.

## ***Table Of Content***

- ## [**imgman**](#imgman)
  - ### [*Table Of Content*](#table-of-content)
  - ### [*Screenshots*](#screenshots)
  - ### [*Background*](#background)
  - ### [*Architecture*](#architecture)
  - ### [*Project Folder Structure*](#project-folder-structure)
  - ### [*Objectives*](#objectives)
  - ### [*Technologies Used*](#technologies-used)
  - ### [*imgman Features*](#imgman-features)
  - ### [*Key features and release dates*](#key-features-and-release-dates)
  - ### [*Project Status*](#project-status)
  - ### [*Running Locally*](#running-locally)
    - ### [*Prerequisites*](#prerequisites)
    - ### [*Clone the repo*](#clone-the-repo)
    - ### [***Create New Virtual Environment***](#create-new-virtual-environment)
    - ### [*Install the requirements*](#install-the-requirements)
    - ### [*Setup Database and make migrations*](#setup-database-and-make-migrations)
  - ### [***Making Contribution***](#making-contribution)
  - ### [*License*](#license)
  - ### [*Code of Conduct*](#code-of-conduct)
  - ### [*Contributors*](#contributors)
  - ### [***Happy Coding***](#happy-coding)

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

## Contributing To The Project

In order to contribute to the project and setup the project locally refer to [Contributing](CONTRIBUTING.md) File.


## License
This Project is Licensed Under [MIT License](LICENSE.md)

## Code of Conduct

Please Follow Our [Code Of Conduct](CODE_OF_CONDUCT.md).

## Contributors

Big thanks to all the [Contributors](https://github.com/kailashchoudhary11/imgman/graphs/contributors)!
<br>
<br>
<a href="https://github.com/kailashchoudhary11/imgman/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kailashchoudhary11/imgman" />
</a>


## Happy Coding
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
