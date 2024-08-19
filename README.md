
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
  - [Prerequisites](#prerequisites)
  - [Docker Image](#docker-image)
  - [Jenkins Pipeline structure](#jenkins-pipeline-structure)
- [Running the Pipeline](#running-the-pipelines)
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
  - **Jenkins**: Install and set up jenkins.


  ## Docker Image

  The Docker image used for the Jenkins pipeline is based on the `jenkins/agent:alpine-jdk11` image and includes Python and Flask. The Docker image can be pulled from DockerHub:

  ```bash
  docker pull mtk3281/docker-python-flask:latest
  ```


  ### Jenkins Pipeline structure

  The Jenkins pipeline script (Jenkinsfile) defines the stages for building, testing, and deploying the Flask application. Below is the pipeline basic structure :

``` groovy
pipeline {
  agent any

  stages {
      stage('Build') {
          steps {
              sh 'echo "Building"'
              // Add commands to build your project here
          }
      }
      stage('Test') {
          steps {
              sh 'echo "Testing"'
              // Add commands to run tests here
          }
      }
      stage('Deploy') {
          steps {
              sh 'echo "Deploying"'
              // Add commands to deploy your application here
          }
      }
  }

  post {
      always {
          // Cleanup steps if needed
      }
      success {
          // Actions to perform when the pipeline succeeds
      }
      failure {
          // Actions to perform when the pipeline fails
      }
  }
}

```

## Running the Pipelines

- **Set up Jenkins**:

  - Create a new pipeline job in Jenkins.
  - Point Jenkins to your repository where Jenskins file is located
  
- **Run the Pipeline**:

  - once the jenkins in configured, you can trigger it manually or set it up to run automatically on each push to the repository.
  
- **Monitor the Pipeline**:

  - Watch the stages execute in Jenkins and check the console output for each stage to ensure everything runs as expected.

- **Deployment**:

  - Customize the Deploy `stage in the Jenkins file `to add your deployment steps.
  

### Project Roadmap

  - Build the Basic Flask Web App Structure
  - Implement Jenkins Tutorials and Explanations
  - Containerize the Application Using Docker
  - Expand Content to Cover Advanced Jenkins Topics
  - Add More Detailed Testing and CI/CD Examples