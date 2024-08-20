from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def recibir_solicitud():
    try:
        response = request.get_json()

        print(json.dumps(response, indent=2))
        return jsonify({"\nmessage": "received"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2222)



