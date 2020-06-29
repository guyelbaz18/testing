pipeline {
    agent { docker { image 'python:3.8' } }
    stages {
        stage('version') {
            steps {
                sh 'python --version'
            }
        }
	stage('test') {
	    steps {
		sh 'sudo python -m pip install --upgrade pip'
          	sh 'sudo pip install pylint'
	        sh 'sudo pip install pytest' 
		sh 'pylint adding.py'
		sh 'pytest tests'
	    }
	}
    }
}
