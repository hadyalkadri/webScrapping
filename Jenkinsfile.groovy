pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/hadyalkadri/webScrapping.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('web-scraper:latest')
                }
            }
        }
        stage('Run Web Scraper') {
            steps {
                script {
                    docker.image('web-scraper:latest').inside {
                        sh 'pip install -r requirements.txt'  // Install Python dependencies
                        sh 'python grabScholarships.py'  // Run the Python web scraper script
                    }
                }
            }
        }
    }
    triggers {
        cron('H/5 * * * *') // Runs every Sunday at midnight
    }
    post {
        always {
            cleanWs()
        }
    }
}
