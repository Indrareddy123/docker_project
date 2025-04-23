pipeline {
    agent any

    stages {
        stage('Trigger Remote Job') {
            steps {
                script {
                    def jenkinsUrl = 'http://localhost:8080/job/chat_bot_ci/build?token=chatbot_build_trigger'
                    sh "curl -X POST ${jenkinsUrl}"
                }
            }
        }
    }
}
