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
          	sh 'pip install pylint --user'
	        sh 'pip install pytest --user' 
		sh 'pylint adding.py'
		sh 'pytest tests'
	    }
	}
    }
}
