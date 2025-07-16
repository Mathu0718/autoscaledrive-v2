pipeline {
  agent any

  stages {
    stage('Clone') {
      steps {
        git 'https://github.com/Mathu0718/autoscaledrive-v2.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        dir('backend') {
          script {
            docker.build('autoscaledrive-backend')
          }
        }
      }
    }

    stage('Run Container') {
      steps {
        sh 'docker run -d -p 5000:5000 autoscaledrive-backend || true'
      }
    }
  }
}
