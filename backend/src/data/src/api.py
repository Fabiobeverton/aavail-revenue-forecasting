from flask import Flask, request, jsonify
from models.model import load_model, predict

app = Flask(__name__)
model = load_model()

@app.route("/predict", methods=["GET"])
def predict_for_country():
    country = request.args.get("country")
    date = request.args.get("date")

    if not country or not date:
        return jsonify({"error": "Both 'country' and 'date' parameters are required."}), 400

    result = predict(model, country, date)
    return jsonify(result)

@app.route("/predict_all", methods=["GET"])
def predict_for_all_countries():
    date = request.args.get("date")
    if not date:
        return jsonify({"error": "The 'date' parameter is required."}), 400

    countries = ["USA", "EIRE", "Germany", "Singapore"]
    results = [predict(model, country, date) for country in countries]
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)