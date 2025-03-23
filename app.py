from flask import Flask, jsonify, render_template
from flask_cors import CORS
import mysql.connector

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)  # Allows frontend to fetch data from backend

# Connect to XAMPP MySQL database
db = mysql.connector.connect(
    host="localhost",  # XAMPP MySQL default host
    user="root",       # Default XAMPP MySQL user
    password="",       # No password by default (leave empty)
    database="real_estate"
)

# Serve the HTML page when accessing "/"
@app.route('/')
def home():
    return render_template("index.html")  # Load index.html

@app.route('/get_agent_ratings', methods=['GET'])
def get_agent_ratings():
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT name, sales, reviews, response_time FROM agents")

        agents = cursor.fetchall()  # Fetch all results
        cursor.close()  # Close cursor

        # AI Rating Calculation
        for agent in agents:
            if agent['reviews'] > 4.5 and agent['sales'] > 60:
                agent['rating'] = "⭐⭐⭐⭐⭐"
            elif agent['reviews'] > 4.0:
                agent['rating'] = "⭐⭐⭐⭐"
            else:
                agent['rating'] = "⭐⭐⭐"

        return jsonify(agents)

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)})

if __name__ == '__main__':
    app.run(debug=True)
