node('docker_agent_python') {

    environment {
        FLASK_APP = 'app.py'
    }

    try {
        stage('Checkout') {
            echo 'git cloning started'
            checkout([$class: 'GitSCM', branches: [[name: 'main']], doGenerateSubmoduleConfigurations: false, extensions: [], userRemoteConfigs: [[url: 'https://github.com/mtk3281/flask-web-app--jenkins']]])
        }

        stage('Install Dependencies') {
            echo 'Installing dependencies...'
            sh 'pip install -r requirements.txt'
        }

        stage('Run Flask App') {
            echo 'Starting the Flask app...'
            sh "nohup python ${FLASK_APP} > app.log 2>&1 &"
            sleep 10
        }

        stage('Test Flask App') {
            echo 'Running tests...'
            sh 'curl -s http://localhost:5000 || exit 1'
            sh 'python -m unittest discover -s tests'
        }

        stage('Clean Up') {
            echo 'Stopping the Flask app...'
            sh "pkill -f 'python ${FLASK_APP}' || true"
        }

        stage('Deploy') {
            echo 'Deploying the Flask app...'
        }

    } catch (Exception e) {
        echo "Build failed: ${e.getMessage()}"
        currentBuild.result = 'FAILURE'
        throw e
    } finally {
        echo 'Cleaning up workspace...'
        deleteDir()
        if (currentBuild.result == 'SUCCESS') {
            echo 'Build succeeded!'
        } else {
            echo 'Build failed!'
        }
    }
}
