from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello f CI/CD Pipeline ! \n New Change Made by ~Govind Jadapalli !"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
