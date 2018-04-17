import os
from flask import json
from flask import jsonify
from flask import Flask
from flask import request
import nomie2to3

app = Flask(__name__)

@app.route("/")
def main():
    return '<p>Nomie conversion tool.</p><p>Paste in all the JSON contents:</p><form action="/convert" method="POST"><textarea name="jsoncontents" id="jsoncontents"></textarea><button>Submit</button></form>'

@app.route("/convert", methods=['POST'])
def convert():
    message = None
    try:
        text = json.dumps(request.json)
        message = request.json('jsoncontents')
    except:
        message = request.form['jsoncontents']
    return nomie2to3.convert(json.loads(message))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 2525))
    app.run(host='0.0.0.0', port=port, debug=True)
