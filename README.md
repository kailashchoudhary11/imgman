![Logo](static/images/logo.png)

## **imgman**

imgman is a unique web app which provides myriad of image manipulation options like blurring of image, black and white filters, converting to pdf, adding grayscale effect, resizing the image. It's built with django, a python web framework.

## ***Table Of Content***:

  - [imgman](#imgman)
  - [Screenshots](#screenshots)
  - [Background](#background)
  - [Architecture](#architecture)
  - [Project Folder Structure](#project-folder-structure)
  - [Objectives](#objectives)
  - [Technologies Used](#technologies-used)
  - [imgman Features](#imgman-features)
  - [Key features and release dates](#key-features-and-release-dates)
  - [Project Status](#project-status)
  - [Making Contribution](#making-contribution)
  - [License](#license)
  - [Contributors](#contributors)
  - [Happy Coding](#happy-coding)

## Screenshots:

![Screenshot (1)]

![Screenshot (2)]

![Screenshot (3)]

## Background:

This project, ***imgman***, is an initiative by [Kailash Choudhary](https://github.com/kailashchoudhary11). It is a platform that allows users to apply unique filters and manipulate images and export them.

## Architecture:

- Django
- img2pdf
- Pillow
- sqlite3
- OpenCV

## Project Folder Structure:

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

## Objectives:

- [x] Create a website that allows users to manipulate images
- [ ] finish the homepage
- [ ] finish the readme
- [ ] other objectives

## Technologies Used:

- HTML/CSS/Javascript (Frontend)
- Django - Framework, Python(Backend)
- GIT (Version Control)
- sqlite3 (Database)

## imgman Features:

- [x] Upload an image
- [ ] choose a filter
- [ ] export the image
- [ ] integrate with other image manipulation libraries

## Key features and release dates:

> Landing page
> Upload Page
> User Dashboard

## Project Status:

> Project is under Development

## Making Contribution:

In order to contribute to the project and setup the project locally refer to [Contributing](CONTRIBUTING.md) File.


## License:

This Project is Licensed Under [MIT License](LICENSE.md)

## Contributors:

Big thanks to all the [Contributors](https://github.com/kailashchoudhary11/imgman/graphs/contributors)!
<br>
<br>
<a href="https://github.com/kailashchoudhary11/imgman/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kailashchoudhary11/imgman" />
</a>


## Happy Coding
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
