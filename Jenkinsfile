pipeline {
    agent any

    environment {
        AWS_REGION = "eu-north-1"
        ECR_REPO = "291159641797.dkr.ecr.eu-north-1.amazonaws.com/myapp"   // replace this
        EC2_IP = "56.228.4.91"    // replace this
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp .'
            }
        }

        stage('Login to ECR') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'aws-cred',
                    usernameVariable: 'AWS_ACCESS_KEY_ID',
                    passwordVariable: 'AWS_SECRET_ACCESS_KEY'
                )]) {
                    sh '''
                    aws ecr get-login-password --region $AWS_REGION \
                    | docker login --username AWS --password-stdin $ECR_REPO
                    '''
                }
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag myapp:latest $ECR_REPO:latest'
            }
        }

        stage('Push to ECR') {
            steps {
                sh 'docker push $ECR_REPO:latest'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sh '''
                ssh -o StrictHostKeyChecking=no ubuntu@$EC2_IP "
                
                aws ecr get-login-password --region $AWS_REGION | \
                docker login --username AWS --password-stdin $ECR_REPO &&
                
                docker pull $ECR_REPO:latest &&
                docker stop myapp || true &&
                docker rm myapp || true &&
                docker run -d -p 5000:5000 --name myapp $ECR_REPO:latest
                
                "
                '''
            }
        }
    }
}
