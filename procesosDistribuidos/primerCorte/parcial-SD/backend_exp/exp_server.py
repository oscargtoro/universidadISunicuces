from flask import Flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def experiment():
    response = jsonify({"error": "Experimental Server encountered an issue"})
    response.status_code = 200
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
