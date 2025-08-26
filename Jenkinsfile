pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building C++ application...'
                sh 'make clean'
                sh 'make'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running Python tests...'
                sh 'python3 tests/test_calculator.py'
            }
        }
        
        stage('Archive') {
            steps {
                echo 'Archiving build artifacts...'
                archiveArtifacts artifacts: 'build/calculator', 
                                 fingerprint: true
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        cleanup {
            echo 'Cleaning up workspace...'
            sh 'make clean'
        }
    }
}