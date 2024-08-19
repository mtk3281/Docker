
<h1 align="center">FLASK-WEB-APP--JENKINS</h1>

<p align="center">
    <em>A Flask web application that provides an introduction to Jenkins, including its architecture, usage, and pipeline creation.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/mtk3281/flask-web-app--jenkins?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
  <img src="https://img.shields.io/github/languages/top/mtk3281/flask-web-app--jenkins?style=flat&color=0080ff" alt="repo-top-language">
  <img src="https://img.shields.io/github/languages/count/mtk3281/flask-web-app--jenkins?style=flat&color=0080ff" alt="repo-language-count">
</p>

<p align="center">
    <em>Developed using the following technologies:</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Flask-000000.svg?style=flat&logo=Flask&logoColor=white" alt="Flask">
</p>

<hr>

## Quick Links

- [Overview](#overview)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Modules](#modules)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
  - [Testing](#testing)
- [Project Roadmap](#project-roadmap)

---

## Overview

This project is a Flask-based web application that provides a comprehensive introduction to Jenkins. It covers Jenkins' architecture, uses, pipeline concepts, and more. The app is containerized using Docker, making it easy to deploy and run.

---

## Features

- **Introduction to Jenkins**: Learn the basics of Jenkins and its importance in CI/CD pipelines.
- **Jenkins Architecture**: Understand the core components of Jenkins.
- **Jenkins Pipeline**: Explore how to create and manage Jenkins pipelines.
- **Docker Integration**: The project is Dockerized for easy setup and deployment.

---

## Repository Structure

```sh
└── flask-web-app--jenkins/
    ├── Dockerfile
    ├── Jenkinsfile
    ├── README.md
    ├── app
    │   ├── __init__.py
    │   ├── routes.py
    │   ├── static
    │   │   ├── css
    │   │   │   └── styles.css
    │   │   └── images
    │   └── templates
    │       ├── about.html
    │       ├── base.html
    │       ├── home.html
    │       ├── jenkins_architecture.html
    │       ├── jenkins_pipeline.html
    │       ├── jenkins_uses.html
    │       └── jenkins_working.html
    ├── app.py
    ├── requirements.txt
    └── tests
        └── test.py
```

---

## Modules

<details closed><summary>Project Structure</summary>

| File                                                                                               | Summary                                      |
| ---                                                                                                | ---                                          |
| [Dockerfile](https://github.com/mtk3281/flask-web-app--jenkins/blob/master/Dockerfile)             | Docker configuration for the project.        |
| [Jenkinsfile](https://github.com/mtk3281/flask-web-app--jenkins/blob/master/Jenkinsfile)           | Jenkins pipeline script.                     |
| [requirements.txt](https://github.com/mtk3281/flask-web-app--jenkins/blob/master/requirements.txt) | Project dependencies.                        |
| [app.py](https://github.com/mtk3281/flask-web-app--jenkins/blob/master/app.py)                     | Entry point for the Flask application.       |

</details>

<details closed><summary>Application Modules</summary>

| File                                                                                     | Summary                                   |
| ---                                                                                      | ---                                       |
| [routes.py](https://github.com/mtk3281/flask-web-app--jenkins/blob/master/app/routes.py)  | Defines the routes for the web application. |

</details>

<details closed><summary>Template Files</summary>

| File                                                                                                                               | Summary                                                             |
| ---                                                                                                                                | ---                                                                 |
| [jenkins_uses.html](https://github.com/mtk3281/flask-web-app--jenkins/blob/master/app/templates/jenkins_uses.html)                 | HTML template explaining Jenkins uses.                              |
| [jenkins_working.html](https://github.com/mtk3281/flask-web-app--jenkins/blob/master/app/templates/jenkins_working.html)           | HTML template explaining how Jenkins works.                         |
| [base.html](https://github.com/mtk3281/flask-web-app--jenkins/blob/master/app/templates/base.html)                                 | Base HTML template for consistent styling.                          |
| [jenkins_architecture.html](https://github.com/mtk3281/flask-web-app--jenkins/blob/master/app/templates/jenkins_architecture.html) | HTML template explaining Jenkins architecture.                      |
| [jenkins_pipeline.html](https://github.com/mtk3281/flask-web-app--jenkins/blob/master/app/templates/jenkins_pipeline.html)         | HTML template explaining Jenkins pipelines.                         |
| [home.html](https://github.com/mtk3281/flask-web-app--jenkins/blob/master/app/templates/home.html)                                 | Home page template for the web application.                         |
| [about.html](https://github.com/mtk3281/flask-web-app--jenkins/blob/master/app/templates/about.html)                               | About page template for the web application.                        |

</details>

---


## Getting Started

### Prerequisites

Ensure you have the following dependencies installed on your system:

- **Docker**: Required to build and run the Docker container.
- **Python**: Ensure Python is installed on your machine.


## Installation

1. **Clone the flask-web-app--jenkins repository:**

    ```sh
    git clone https://github.com/mtk3281/flask-web-app--jenkins
    ```

2. **Change to the project directory:**

    ```sh
    cd flask-web-app--jenkins
    ```

3. **Install the dependencies:**

    Create a virtual environment and install the required Python packages:

    ```sh

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```



### Running flask-web-app--jenkins

Use the following command to run the Flask web app:

```sh
docker build -t jenkins-flask-app .
docker run -p 5000:5000 jenkins-flask-app
```

This will build the Docker image and run the Flask application, making it accessible at http://127.0.0.1:5000.

### Tests

To execute tests, run:

``` sh
python -m unittest discover -s app/test
```

---

Project Roadmap

- ** Build the basic Flask web app structure **
- ** Implement Jenkins tutorials and explanations **
- ** Containerize the application using Docker **
- ** Expand content to cover advanced Jenkins topics **
- ** Add more detailed testing and CI/CD examples **


---
