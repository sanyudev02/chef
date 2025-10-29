pipeline{
    agent any
    environment{
        PYTHON="C:\\Users\\sanyu\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
    }
    stages{
        stage("Checkout code"){
            steps{
                checkout scm
            }
        }
        stage("Install dependencies"){
            steps{
                bat "${env.PYTHON} -m pip install -r requirements.txt"
            }

        }
        stage("Extract data"){
            steps{
                bat "${env.PYTHON} extract_data.py"
            }

        }
    }
}