from flask import Flask, request, jsonify,render_template
from chat import get_response

app = Flask(__name__)

@app.get('/')
def index():
    return render_template("base.html")


@app.post('/predict')
def predict():
    text = request.json.get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)