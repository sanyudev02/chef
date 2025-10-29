pipeline{
    agent any
    environment{
        PYTHON="C:\\Users\\sanyu\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
        APP_TOKEN=credentials("1234")
    }
    stages{
        stage("Checkout code"){
            steps{
                git url:'https://github.com/sanyudev02/chef.git',branch:'main'
            }
        }
        stage("Install dependencies"){
            steps{
                bat "%PYTHON% -m pip install -r requirements.txt"
            }

        }
        stage("Extract data"){
            steps{
                bat """
                SET TOKEN=${env.APP_TOKEN}"
                ${env.PYTHON} extract_data.py
                """
            }

        }
    }
}