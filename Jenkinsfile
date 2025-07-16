pipeline {
  agent any

  stages {
    stage('Clone') {
      steps {
        git branch: 'main', url: 'https://github.com/Mathu0718/autoscaledrive-v2.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t autoscaledrive-backend backend/'
      }
    }

    stage('Run Container') {
      steps {
        sh 'docker run -d -p 5000:5000 autoscaledrive-backend || true'
      }
    }
  }
}
