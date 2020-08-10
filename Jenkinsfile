pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                awsCodeBuild projectName: 'push-to-ECR', credentialsType: 'keys', region: 'us-east-1', sourceControlType: 'project'
                echo 'Done................'
            }
        }
    }
}

