pipeline {
    agent any

    environment {
        IMAGE_NAME = "akshay1092003/python-app"
    }

    stages {

        stage('Git Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Gitleaks Scan') {
            steps {
                sh 'gitleaks detect --source . -v'
            }
        }

        stage('SonarQube Scan') {
    steps {
        script {
            def scannerHome = tool 'sonar-scanner'
            withSonarQubeEnv('sonar') {
                sh "${scannerHome}/bin/sonar-scanner"
            }
        }
    }
}

        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Trivy Scan') {
            steps {
                sh 'trivy image --severity HIGH,CRITICAL $IMAGE_NAME'
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push $IMAGE_NAME'
                }
            }
        }
        
        stage('Remove Old Container') {
            steps {
                sh 'docker rm -f python-app || true'
            }
        }

        // OPTIONAL DEPLOYMENT STAGE
        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name python-app $IMAGE_NAME'
            }
        }
    }

    post {
        success {
            echo 'Pipeline SUCCESS'
        }
        failure {
            echo 'Pipeline FAILED'
        }
    }
}
