pipeline {
    agent any

    stages {
        stage('Trigger Remote Job') {
            steps {
                script {
                    // Print the message to the Jenkins console
                    echo 'Hello, how can I help?'

                    // Set Jenkins URL and token for remote job triggering
                    def jenkinsUrl = 'http://localhost:8081/job/chat_bot_ci/build?token=chatbot_build_trigger'
                    
                    // Trigger the remote job using curl
                    try {
                        sh "curl -X POST ${jenkinsUrl}"
                        echo "Remote job triggered successfully"
                    } catch (Exception e) {
                        echo "Failed to trigger the remote job: ${e.getMessage()}"
                    }
                }
            }
        }
    }
}
