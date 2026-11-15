pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest --junitxml=test-reports/results.xml
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'test-reports/results.xml,coverage.xml,htmlcov/**', allowEmptyArchive: true
                }
            }
        }

        stage('Docs') {
            steps {
                sh 'ls -la docs/'
                echo 'Документация: docs/calculator.md'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'docs/**', allowEmptyArchive: true
                }
            }
        }
    }
}
