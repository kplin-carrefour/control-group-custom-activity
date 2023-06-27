from flask import Flask, request
import secrets

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.post('/publish')
def publish():
    return ""

@app.post('/execute')
def execute():
    root = request.json.get('root')
    journeyVersionId = root.journeyId
    subscriberKey = root.keyValue

    grupoControle = secrets.randbelow(10) >= 9 #10%

    #upsert in DataExtension

    if grupoControle is True:
        return { branchResult: "grupo-controle", j: journeyVersionId, s: subscriberKey }
    else:
        return { branchResult: "audiencia", j: journeyVersionId, s: subscriberKey }
