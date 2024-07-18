from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def recibir_solicitud():
    try:
        datos = request.get_json()
        # Procesa los datos de la solicitud aquí
        print("JSON received:")
        print(datos)
        # Puedes realizar acciones adicionales aquí según tus necesidades

        # Responde con un mensaje de confirmación
        return jsonify({"message": "received"})
        # Puedes realizar acciones adicionales aquí según tus necesidades

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2223)



