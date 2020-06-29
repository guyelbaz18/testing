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
          	sh 'pip install pylint --no-cache-dir'
	        sh 'pip install pytest --no-cache-dir' 
		sh 'pylint adding.py'
		sh 'pytest tests'
	    }
	}
    }
}
