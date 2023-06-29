from flask import Flask, request
import secrets

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.post('/save')
def save():
    return ""

@app.post('/publish')
def publish():
    return ""

@app.post('/validate')
def validate():
    return ""

@app.post('/stop')
def stop():
    return ""

@app.post('/execute')
def execute():
    #root = request.json['root']
    #journeyVersionId = root['journeyId']
    #subscriberKey = root['keyValue']

    grupoControle = secrets.randbelow(10) >= 9 #10%

    #upsert in DataExtension

    if grupoControle is True:
        return { "branchResult": "controle" }
    else:
        return { "branchResult": "tratamento" }
