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
                sh 'export PYTHONPATH=/home/ubuntu/.local/lib/python3.6/site-packages/'
                sh 'python3 invoke_sfn.py'
            }
        }
    }
}

