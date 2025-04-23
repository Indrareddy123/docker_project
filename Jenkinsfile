pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/Indrareddy123/docker_project.git'
        CREDENTIALS_ID = 'github-pat-2'
        PYTHON_ENV = 'chatbot_venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: "${CREDENTIALS_ID}", url: "${REPO_URL}", branch: 'main'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv ${PYTHON_ENV}
                    source ${PYTHON_ENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    source ${PYTHON_ENV}/bin/activate
                    pytest tests/
                '''
            }
        }

        stage('Build Chatbot') {
            steps {
                echo 'Building chatbot application...'
                // Add your build steps here if needed
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to staging environment...'
                // Add your deployment commands here
            }
        }

        stage('Run Post-Deployment Tests on Staging') {
            steps {
                echo 'Running post-deployment tests...'
                // Add your test logic here
            }
        }

        stage('Deploy to Production') {
            steps {
                echo 'Deploying to production...'
                // Add production deployment steps
            }
        }
    }

    post {
        failure {
            echo 'Chatbot deployment failed!'
        }
        success {
            echo 'Chatbot deployed successfully!'
        }
    }
}
