pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages{
        stage('Cloning GitHub repo to Jenkins'){
            steps{
                echo 'Cloning GitHub repo to Jenkins...'
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/udayaKherath/MLOPS-PROJECT-1.git']])
            }
        }

        stage('Setting up our Virtual Environment and Installing dependencies'){
            steps{
                echo 'Setting up our Virtual Environment and Installing dependencies...'
                sh '''
                python -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -e .
                '''
            }
        }
    }
}