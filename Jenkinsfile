pipeline {
    agent any

    environment {
        IMAGE_NAME = 'chatbot-image'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: 'github-pat', url: 'https://github.com/Indrareddy123/chatbot-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    dockerImage.run("-d --name chatbot-container")
                }
            }
        }
    }
}
