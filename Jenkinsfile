pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/GoviGt650/jenkins-test.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop myapp || true
                docker rm myapp || true
                docker run -d -p 5000:5000 --name myapp myapp
                '''
            }
        }
    }
}
