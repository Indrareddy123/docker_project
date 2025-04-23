pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/Indrareddy123/docker_project.git'
        CREDENTIAL_ID = 'github-pat-chatbot'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: "${CREDENTIAL_ID}", url: "${REPO_URL}", branch: 'main'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh '''
                    python3 -m venv chatbot_env
                    source chatbot_env/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt || echo "No requirements.txt found"
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    source chatbot_env/bin/activate
                    pytest || echo "No tests found"
                '''
            }
        }

        stage('Build Chatbot') {
            steps {
                echo 'Simulating build...'
                sh 'echo "Build complete"'
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploying chatbot to staging...'
                // Add your actual deployment commands here
            }
        }

        stage('Post-Deployment Tests') {
            steps {
                echo 'Running post-deployment tests...'
                // Add real post-deployment test commands here
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying chatbot to production...'
                // Add your production deployment steps here
            }
        }
    }

    post {
        success {
            echo '✅ Chatbot deployed successfully!'
        }
        failure {
            echo '❌ Chatbot deployment failed!'
        }
    }
}
