pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'chmod 777 build_and_push.sh'
                sh './build_and_push.sh sagemaker-tf-cifar10-example'
            }
        }
        stage('deploy') {
            steps {
                sh 'id'
                sh 'python3 invoke_sfn.py'
            }
        }
    }
}

