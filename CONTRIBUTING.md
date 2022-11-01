# Contributing Guidelines

Before contributing, please read our [Code of Conduct](CODE_OF_CONDUCT.md) .

## Figma Design Link

- [Figma Link](https://www.figma.com/file/N1GUOSfNsqb8NTInxXj75K/Imgman-Project?node-id=0%3A1)

## CSS BEM Convention

We use BEM (Block, Element, Modifier) Convention,
please read documentation to keep css in order: [CSS B.E.M. Convention Documentation](https://getbem.com/) .

## Installation and Usage

- ### Prerequisites

  - Python >= 3.8

  - VS Code or any other IDE

- ### Fork the Repository

  Click on the fork button on the upper right corner to fork the repository.

- ### Clone the Repository

  ```bash
  git clone https://github.com/{your-github-username}/imgman.git

  cd imgman
  ```

- ### Create and Activate New Virtual Environment

  Refer to this [guide](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) or follow the below steps!

  ```bash
  python -m venv venv
  ```

  - Windows

    ```bash
    .\venv\Scripts\activate
    ```

  - Linux / Mac
    ```bash
    source venv/bin/activate
    ```

  **_note: you should be on the same dir as requirements.txt file_**

- ### Install the requirements

  ```bash
  pip install -r requirements.txt
  ```

- ### Create .env File

  This project uses the [Cloudinary](https://cloudinary.com) service to store images. You can create a free account [here](https://cloudinary.com/users/register/free) and get your API keys.

  Then, create a new .env file same as the [.env.example](.env.example) file and fill in the required fields.

- ### Create Database and Tables

  ```bash
  python manage.py migrate
  ```

- ### Run the Django Server

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

We use GitHub issues to track public bugs.

Please ensure your description is
clear and has sufficient instructions to be able to reproduce the issue.

## License

By contributing to imgman, you agree that your contributions will be licensed under the LICENSE file in
the root directory of this source tree.
