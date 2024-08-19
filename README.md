# Jenkins Basics Flask Web App

This project is a Flask web application designed to explain the basics of Jenkins, including its working, uses, architecture, and pipelines. It also includes a Dockerfile for building a Docker image that can be used as a Docker cloud agent (slave) for building projects.

## Project Structure

- `flask_app/`
  - `app/`
    - `static/`
      - `css/`
        - `style.css`  # Contains CSS styles for the web app
      - `images/`
        - Various image files  # Contains images used in the web app
    - `templates/`
      - HTML files for each route describing Jenkins' working
  - `__init__.py`  # Initializes the Flask app
  - `routes.py`  # Contains route definitions for the Flask app
  - `test/`
    - `test.py`  # Contains unit tests for the Flask app
- `app.py`  # Main file to run the Flask app
- `Dockerfile`  # Dockerfile to create the Docker image
- `requirements.txt`  # Lists the required dependencies for the project
- `jenkinsfile`  # Contains the Jenkins pipeline script

## Features

- **Flask Web Application**: Provides information about Jenkins, including:
  - **What is Jenkins**: Introduction to Jenkins
  - **How does it work**: Explanation of Jenkins' working
  - **Uses of Jenkins**: Various uses and benefits of Jenkins
  - **Jenkins Architecture**: Overview of Jenkins' architecture
  - **Pipeline Working**: Basics of Jenkins pipelines

- **Docker Integration**: 
  - **Dockerfile**: Builds a Docker image that can be used as a Docker cloud agent (slave) for Jenkins.

## Getting Started

### Prerequisites

- Docker: Ensure Docker is installed on your machine.

### Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/mtk3281/flask-web-app.git
   cd flask-web-app


2. **Install Dependencies:**

    Create a virtual environment and install the required Python packages:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Run the Flask Application:**

    ```bash
    python app.py
    ```

    The application will be accessible at [http://127.0.0.1:5000](http://127.0.0.1:5000).

4. **Build and Run Docker Container:**

    ```bash
    docker build -t jenkins-flask-app .
    docker run -p 5000:5000 jenkins-flask-app
    ```

    This will build the Docker image and run it, making the Flask application accessible at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### Testing

To run the unit tests:

```bash
python -m unittest discover -s app/test

