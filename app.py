# app.py
from flask import Flask, request, render_template, jsonify
from fitness_dietplanner import (
    generate_fitness_plan,
    calculate_bmi,
    generate_diet_plan,
    meal_plan_customization,
    water_intake_tracker,
    save_progress,
    get_progress_history
)
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Route to serve the HTML page
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Route to handle form submission
@app.route("/process", methods=["POST"])
def process():
    try:
        data = request.json

        # Extract user inputs
        name = data.get("name")
        age = int(data.get("age"))
        weight = float(data.get("weight"))
        height = float(data.get("height"))
        activity_level = data.get("activity_level").lower()
        fitness_goal = data.get("fitness_goal").lower()
        dietary_preference = data.get("dietary_preference").lower()

        # Generate results
        bmi_result = calculate_bmi(weight, height)
        fitness_plan = generate_fitness_plan(activity_level, fitness_goal)
        diet_plan = generate_diet_plan(weight, height, age, activity_level, fitness_goal, dietary_preference)
        meal_plan = meal_plan_customization(dietary_preference)
        water_intake = water_intake_tracker(weight, activity_level)

        response_data = {
            "bmi": bmi_result,
            "fitness_plan": fitness_plan,
            "diet_plan": diet_plan,
            "meal_plan": meal_plan,
            "water_intake": water_intake
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to handle progress updates
@app.route("/update-progress", methods=["POST"])
def update_progress():
    try:
        data = request.json
        name = data.get("name")
        current_weight = float(data.get("current_weight"))
        date = data.get("date")
        notes = data.get("notes", "")

        save_progress(name, current_weight, date, notes)
        return jsonify({"message": "Progress updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get progress history
@app.route("/get-progress/<name>", methods=["GET"])
def get_progress(name):
    try:
        progress_data = get_progress_history(name)
        return jsonify(progress_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)