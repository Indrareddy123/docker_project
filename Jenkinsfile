pipeline {
    agent any

    environment {
        IMAGE_NAME = 'chatbot-image'
        CONTAINER_NAME = 'chatbot-container'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Indrareddy123/docker_project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Deploy Locally') {
            steps {
                script {
                    sh """
                        docker stop ${CONTAINER_NAME} || true
                        docker rm ${CONTAINER_NAME} || true
                        docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}
                    """
                }
            }
        }
    }
}
