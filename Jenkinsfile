pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Anushka291/Practice-DevOps.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run App') {
            steps {
                bat 'python app.py'
            }
        }
    }
}
