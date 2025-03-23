from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import mysql.connector
import joblib  # For loading AI model
import numpy as np

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# Load AI model & encoder
model = joblib.load("rating_model.pkl")  # Pre-trained model
encoder = joblib.load("encoder.pkl")  # Label encoder for response time

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="real_estate"
)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get_agent_ratings', methods=['GET'])
def get_agent_ratings():
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT name, sales, reviews, response_time FROM agents")

        agents = cursor.fetchall()
        cursor.close()

        for agent in agents:
            agent['rating'] = "⭐" * int(round(agent['reviews']))  # Basic star rating

        return jsonify(agents)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)})

# 🔹 New Route: Predict AI Rating
@app.route('/predict_rating', methods=['POST'])
def predict_rating():
    try:
        data = request.get_json()
        sales = float(data["sales"])
        reviews = float(data["reviews"])
        response_time = data["response_time"]

        # Convert response time to numerical encoding
        response_encoded = encoder.transform([response_time])[0]

        # Prepare input for AI model
        input_data = np.array([[sales, reviews, response_encoded]])

        # Predict AI rating
        prediction = model.predict(input_data)[0]
        rating = "⭐" * int(round(prediction))  # Convert to star rating

        return jsonify({"rating": rating})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
