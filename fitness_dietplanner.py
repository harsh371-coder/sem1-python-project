import csv
import os
from datetime import datetime

def calculate_bmi(weight, height):
    height_in_m = height / 100
    bmi = weight / (height_in_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    else:
        category = "Overweight"
    return {"bmi": round(bmi, 2), "category": category}


def generate_fitness_plan(activity_level, fitness_goal):
    plan = []
    if fitness_goal == "weight loss":
        if activity_level == "sedentary":
            plan.append("Start with low-impact activities like walking or light cardio for 30 minutes daily.")
        elif activity_level == "lightly active":
            plan.append("Do moderate cardio for 30-45 minutes 3-4 times a week, like brisk walking, jogging.")
            plan.append("Do little Strength Training like Wall Pushups, Seated Squats,Plank for 30-45 minutes 3-4 times a week")
        else:
            plan.append("Do intense cardio 5 times a week, like Running, Swimming.")
            plan.append("Do Strength Training like Pushups, Squats, Cable Rows, Plank for 30-45 minutes 4-5 times a week.")
    elif fitness_goal == "muscle gain":
        if activity_level == "sedentary":
                plan.append("Do little Strength Training like Wall Pushups, Seated Squats,Plank for 30-45 minutes 3-4 times a week")
        elif activity_level == "lightly active":
            plan.append("Do moderate cardio for 30-45 minutes 1-2 times a week, like brisk walking, jogging.")
            plan.append("Do little Strength Training like Wall Pushups, Seated Squats,Plank for 30-45 minutes 3-4 times a week")
        else:
            plan.append("Do cardio 2-3 times a week like Running and Swimming.")
            plan.append("Do Strength Training like Pushups, Squats, Cable Rows, Plank for 30-45 minutes 4-5 times a week.")
    else:
        plan.append("Follow a balanced routine with strength training and cardio.")
        plan.append("Do Strength Training like Pushups, Squats, Cable Rows, Plank for 30-45 minutes 4-5 times a week.")
        plan.append("Run for 30 minutes a day and focus on your diet.")
    return plan


def generate_diet_plan(weight, height, age, activity_level, fitness_goal, dietary_preference):
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
    if activity_level == "sedentary":
        calories = bmr * 1.2
    elif activity_level == "lightly active":
        calories = bmr * 1.375
    elif activity_level == "moderately active":
        calories = bmr * 1.55
    else:
        calories = bmr * 1.725
    if fitness_goal == "weight loss":
        calories -= 500
    elif fitness_goal == "muscle gain":
        calories += 500
    return {
        "calories": round(calories, 2),
        "dietary_recommendation": dietary_preference,
    }


def water_intake_tracker(weight, activity_level):
    if activity_level == "sedentary":
        water_intake = weight * 30
    elif activity_level == "lightly active":
        water_intake = weight * 35
    elif activity_level == "moderately active":
        water_intake = weight * 40
    else:
        water_intake = weight * 45
    return {"water_intake_liters": round(water_intake / 1000, 2)}


def meal_plan_customization(dietary_preference):
    meal_plan = {}
    if dietary_preference == "vegetarian":
        meal_plan = {
            "breakfast": "Oatmeal with fruits and nuts.",
            "lunch": "Lentil salad with quinoa.",
            "dinner": "Grilled paneer with vegetables."
        }
    elif dietary_preference == "vegan":
        meal_plan = {
            "breakfast": "Smoothie with almond milk.",
            "lunch": "Quinoa and chickpea bowl.",
            "dinner": "Tofu stir-fry with brown rice."
        }
    elif dietary_preference == "gluten-free":
        meal_plan = {
            "breakfast": "2-3 eggs Season with salt, pepper, and a pinch of paprika.",
            "lunch": "Grilled Chicken Salad with Quinoa.",
            "dinner": "Baked Salmon with Steamed Veggies.",
        }
    elif dietary_preference == "no preference":
        meal_plan = {
            "breakfast": "Choice of eggs or oatmeal with fruits",
            "lunch": "Grilled chicken or fish with vegetables",
            "dinner": "Lean protein with whole grains and vegetables"
        }
    return meal_plan


def save_progress(name, current_weight, date, notes):
    """
    Save user's progress to a CSV file
    """
    # Create a 'progress' directory if it doesn't exist
    progress_dir = 'progress'
    if not os.path.exists(progress_dir):
        os.makedirs(progress_dir)
    
    filename = os.path.join(progress_dir, f'progress_{name.lower()}.csv')
    file_exists = os.path.exists(filename)
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Date', 'Weight', 'Notes'])
        writer.writerow([date, current_weight, notes])


def get_progress_history(name):
    """
    Retrieve user's progress history from CSV file
    """
    progress_dir = 'progress'
    filename = os.path.join(progress_dir, f'progress_{name.lower()}.csv')
    progress_data = []
    
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            progress_data = list(reader)
    
    return progress_data