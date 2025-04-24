pipeline {
    agent any

    environment {
        IMAGE_NAME = "indraaavula/chatbot-container-interactive-v2"
        TAG = "latest"
    }

    stages {
        stage('Clone Repo') {
            steps {
                // Use the correct branch here if needed
                git branch: 'main', url: 'https://github.com/Indrareddy123/docker_project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-creds', url: '']) {
                    script {
                        docker.image("${IMAGE_NAME}:${TAG}").push()
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh "docker rm -f chatbot-deploy || true"
                    sh "docker run -d --name chatbot-deploy ${IMAGE_NAME}:${TAG}"
                }
            }
        }
    }
}
