pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "chatbot:latest"
        DOCKER_REGISTRY = "your_docker_registry_url"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    // Run the container
                    sh 'docker run -d -p 5000:5000 ${DOCKER_IMAGE}'
                }
            }
        }
        stage('Test Chatbot') {
            steps {
                script {
                    // Add test steps to verify if the chatbot is working
                    // Example: curl to check the chatbot's response
                    sh 'curl http://localhost:5000/test-endpoint'
                }
            }
        }
        stage('Clean Up') {
            steps {
                script {
                    // Clean up by stopping and removing the container
                    sh 'docker ps -q --filter "ancestor=${DOCKER_IMAGE}" | xargs docker stop | xargs docker rm'
                }
            }
        }
    }
}
