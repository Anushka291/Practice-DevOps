pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
    }
        stage('Run App') {
            steps {
                timeout(time: 60, unit: 'SECONDS')
                {
                    bat 'python app.py'
                }
        }
    }
}
