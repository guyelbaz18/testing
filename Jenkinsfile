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
		sh 'python -m venv myenv'
		sh 'source myenv/bin/activate'
          	sh 'pip install pylint'
	        sh 'pip install pytest' 
		sh 'pylint adding.py'
		sh 'pytest tests'
	    }
	}
    }
}
