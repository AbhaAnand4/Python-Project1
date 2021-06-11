pipeline {
    agent any
    stages {
        stage('Code Checkout') {
            steps {
                // Checkout code from git
                git branch: 'main', url: 'https://github.com/AbhaAnand4/assignment.git'
            }
        }
        stage('input1') {
            steps {
                // Run input1 test
                sh 'python3 printip/ip_print.py examples/input1.json'
            }
        }
        stage('input2') {
            steps {
                // Run input2 test
                sh 'python3 printip/ip_print.py examples/input2.json'
            }
        }
    }
}
