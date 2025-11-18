pipeline {
    agent none

    environment {
        DOCKERHUB_USER = 'yourusername'
        DOCKERHUB_REPO = 'flask-app'
    }

    stages {
        stage('Build Image on node1') {
            agent { label 'node1' }

            steps {
                echo "Building Docker image on node1..."

                sh '''
                docker build -t $DOCKERHUB_USER/$DOCKERHUB_REPO:latest .
                echo "$DOCKER_PASSWORD" | docker login -u "$DOCKERHUB_USER" --password-stdin
                docker push $DOCKERHUB_USER/$DOCKERHUB_REPO:latest
                '''
            }
        }

        stage('Deploy on node2') {
            agent { label 'node2-deploy' }

            steps {
                echo "Deploying Flask app on node2..."

                sh '''
                docker pull $DOCKERHUB_USER/$DOCKERHUB_REPO:latest

                docker stop flask-app || true
                docker rm flask-app || true

                docker run -d -p 5000:5000 \
                    --name flask-app \
                    $DOCKERHUB_USER/$DOCKERHUB_REPO:latest
                '''
            }
        }
    }
}
