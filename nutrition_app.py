import streamlit as st
import pandas as pd
import joblib

pipeline = joblib.load("nutrition_model.pkl")

def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)

def get_health_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Normal"
    elif bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def meal_plan_calories(total_calories, meals, snacks):
    plan = {}
    if meals == 3:
        plan['Breakfast'] = total_calories * 0.25
        plan['Lunch'] = total_calories * 0.40
        plan['Dinner'] = total_calories * 0.30
        if snacks >= 1:
            plan['Snack'] = total_calories * 0.05
    elif meals == 2 and snacks == 1:
        plan['Meal1'] = total_calories * 0.35
        plan['Meal2'] = total_calories * 0.50
        plan['Snack'] = total_calories * 0.15
    elif meals == 1 and snacks == 2:
        plan['Meal'] = total_calories * 0.50
        plan['Snack1'] = total_calories * 0.25
        plan['Snack2'] = total_calories * 0.25
    return plan


st.title("Smart Nutrition Recommendation System")
st.write("Enter your details to get a personalized nutrition plan!")

age = st.number_input("Age", min_value=0,max_value=1000,value=0)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
height = st.number_input("Height (cm)", min_value=0,max_value=1000,value=1)
weight = st.number_input("Weight (kg)", min_value=0,max_value=1000,value=0)
goal = st.selectbox("Goal", ["Weight Loss", "Muscle Gain", " Maintenance"])
diet_type = st.selectbox("Diet Type", ["Vegan", "Vegetarian", "Non-Vegetarian"])
activity_level = st.selectbox("Activity Level", ["Low", "Moderate", "High"])

bmi = calculate_bmi(weight, height)
health_cat = get_health_category(bmi)
st.write(f"**Your BMI:** {bmi:.2f} ({health_cat})")

if st.button("Get Nutrition Plan"):
    
    user_df = pd.DataFrame([{
        "Age": int(age),
        "Gender": gender,
        "Height_cm": float(height),
        "Weight_kg": float(weight),
        "BMI": bmi,
        "Health_Category": health_cat,
        "Activity_Level": activity_level,
        "Goal": goal,
        "Diet_Type": diet_type
    }])
    
    user_df = user_df[pipeline.feature_names_in_]
    
    prediction = pipeline.predict(user_df)
    calories, protein, carbs, fats = prediction[0]
    
    st.subheader("Recommended Daily Intake")
    total_calories=int(calories)
    st.write(f"**Estimated daily calories:** {calories:.2f} kcal")
    st.write(f"**Protein:** {protein:.2f} g")
    st.write(f"**Carbs:** {carbs:.2f} g")
    st.write(f"**Fats:** {fats:.2f} g")

    st.write("*Tip:* drink water before eating and include more vegetables*")
    st.write("*Tip:* Maintain a balanced diet with regular hydration*")

    if bmi < 18.5:
        meals, snacks = 3, 2
    elif 18.5 <= bmi <= 24.9:
        meals, snacks = 3, 0
    elif 25 <= bmi <= 29.9:
        meals, snacks = 2, 1
    else:
        meals, snacks = 1, 2

    st.write(f"**Based on your BMI, you can plan:** {meals} main meals + {snacks} snacks per day")

