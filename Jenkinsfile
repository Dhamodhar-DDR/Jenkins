pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Dhamodhar-DDR/Jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x square.py"
                sh "./square.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x test.py"
                sh "./test.py"
            }
        }
    } 
}
