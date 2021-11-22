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
                sh "chmod u+x prog.py"
                sh "./prog.py"
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