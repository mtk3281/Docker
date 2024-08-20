pipeline {
    agent {
        label 'docker_python'
    }

    environment {
        FLASK_APP = 'app.py'
    }

    stages {
        stage('Verify Git Installation') {
            steps {
                echo ' Verifying Git installation...'
                script {
      
                    sh 'if [ -x "/usr/bin/git" ]; then echo "Git is installed at /usr/bin/git"; else echo "Git is not installed"; exit 1; fi'
                }
            }
        }

        stage('Checkout') {
            steps {
               checkout([$class: 'GitSCM',
                userRemoteConfigs: [[url: 'https://github.com/mtk3281/flask-web-app--jenkins.git']],
                branches: [[name: '*/main']],
                extensions: []
            ])

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
