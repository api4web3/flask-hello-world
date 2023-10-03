from flask import Flask
from db import connectDb
from getip import getIp

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = getIp() + " " + connectDb()
    return response

if __name__ == "__main__":
    app.run(debug=True)
