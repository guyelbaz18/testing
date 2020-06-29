pipeline {
    agent { docker 
		{ image 'python:3.8' 
		  args '-u root:root' 
		}
	  }
    stages {
        stage('version') {
            steps {
                sh 'python --version'
            }
        }
	stage('test') {
	    steps {
          	sh 'pip install pylint'
	        sh 'pip install pytest' 
		sh 'pylint adding.py'
		sh 'pytest tests'
	    }
	}
    }
}
