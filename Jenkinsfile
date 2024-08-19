pipeline {
    agent {
        label 'docker_agent_python'
    }

    environment {
        FLASK_APP = 'app.py'
    }

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Starting Git clone...'
                git branch: 'main', changelog: false, poll: false, url: 'https://github.com/mtk3281/flask-web-app--jenkins'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                echo 'Starting the Flask app...'
                sh 'nohup python $FLASK_APP > app.log 2>&1 &'
                sleep time: 10, unit: 'SECONDS'
            }
        }

        stage('Test Flask App') {
            steps {
                echo 'Running tests...'
                sh 'curl -s http://localhost:5000 || exit 1'
                sh 'python -m unittest discover -s tests'
            }
        }

        stage('Clean Up') {
            steps {
                echo 'Stopping the Flask app...'
                sh 'pkill -f "python $FLASK_APP" || true'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the Flask app...'
                // Add your deployment steps here
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            deleteDir()
        }

        success {
            echo 'Build succeeded!'
        }

        failure {
            echo 'Build failed!'
        }
    }
}
