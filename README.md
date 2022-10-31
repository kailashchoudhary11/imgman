![Logo](static/images/logo.png)

## Join Our Discord Community

[![Discord Server](https://discordapp.com/api/guilds/1033034001260236910/widget.png?style=banner3)](https://discord.gg/GWvNKAKkJS)

## [**imgman**](https://imgman.herokuapp.com/)

imgman is a unique web app which provides myriad of image manipulation options like blurring of image, black and white filters, converting to pdf, adding grayscale effect, resizing the image. It's built with django, a python web framework.

You can visit the website over [**here**](https://imgman.herokuapp.com/)

## ***Table Of Content***:

  - [imgman](#imgman)
  - [Getting Started](#getting-started)
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

## Getting started:

In order to get you started, just make sure to check out our [Contributing](CONTRIBUTING.md) file. 

There you will find the instructions to build your environment and run the app!

## Screenshots:

![screencapture-imgman-herokuapp-sinimg-upload-2022-10-23-08_58_56](https://user-images.githubusercontent.com/49649259/197379292-8698a66b-8fa1-496f-96a8-8e25bae50011.png)


<div align="center">
 <p> Uploaded base image: </p>
<img src="https://user-images.githubusercontent.com/49649259/197379319-9bc54f61-138c-4653-8b32-21e7dbfa216c.jpg" />
    
 <p> Results: </p>
    <img width="220" src="https://user-images.githubusercontent.com/49649259/197379351-c27e3266-163d-4270-bd8e-f8343d292a9f.png" />
    <img width="220" src="https://user-images.githubusercontent.com/49649259/197379420-e486bf9d-e6d7-41fa-b74e-d9234f4b268d.png" />
    <img width="220" src="https://user-images.githubusercontent.com/49649259/197379415-7f598819-cc75-4dd7-876e-affaa937ec7f.png" />
    <img width="220" src="https://user-images.githubusercontent.com/49649259/197379417-4cdb11cf-ab26-4a67-9e04-e2a829d9f1d9.png" />
  </div>
</div>

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
- [ ] Choose a filter
- [ ] Add Black & White filter
- [ ] Add Grayscale effect
- [ ] Image blur effect
- [ ] Convert to pdf
- [ ] Export the image
- [ ] Integrate with other image manipulation libraries .

## Key features and release dates:

> Landing page
> Upload Page
> User Dashboard

## Project Status:

> Project is under Development

## Making Contribution:

In order to contribute to the project and setup the project locally refer to [Contributing](CONTRIBUTING.md) File.

Also Please Join our [Discord Server](https://discord.gg/GWvNKAKkJS) For Discussion Related to the project!

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
