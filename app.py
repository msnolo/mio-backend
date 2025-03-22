from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    print("New message from:", data["nome"])
    print("Email:", data["email"])
    print("Message:", data["messaggio"])
    return jsonify({"message": "Message received successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
