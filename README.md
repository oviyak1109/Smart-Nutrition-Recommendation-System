## Smart Nutrition Recommendation System

## Overview
This project demonstrates an **AI-powered nutrition recommendation system** that predicts **daily calorie intake, protein, carbohydrates, and fats** based on user health data.  
It calculates **BMI**, categorizes **health status**, and provides the recommended **meal and snack counts per day**.  


---

## Tools & Technologies
- **Python** – Data processing, BMI calculation, and ML pipeline  
- **Scikit-Learn** – Linear Regression, Pipeline, OneHotEncoder  
- **Pandas & NumPy** – Data manipulation and preprocessing  
- **Joblib** – Saving and loading trained ML models  
- **Streamlit** - For web interface  

---

## Workflow
1. **Data Preparation**
   - Load dataset (`Advanced_Diet_Recommender_Dataset.csv`) and handle missing values.  
   - Separate features (user inputs) and target variables (calories, protein, carbs, fats).  

2. **Feature Engineering**
   - Calculate BMI from height and weight.  
   - Categorize BMI into **health categories** (Underweight, Normal, Overweight, Obese).  
   - Encode categorical variables like **Gender, Activity Level, Goal, and Diet Type**.  

3. **Model Training**
   - Train a **Linear Regression model** using a **scikit-learn Pipeline**.  
   - Evaluate model performance using **R²** and **RMSE** metrics.  
   - Save the trained model as `nutrition_model.pkl` for predictions.  

4. **Prediction**
   - Input user details to predict **daily calories, protein, carbs, and fats**.  
   - Suggest **number of meals and snacks per day** based on BMI.  

5. **Deployment**
   - Display predictions and meal/snack count by collecting user information using a web interface(Streamlit).  

---

## Results
- Built an **end-to-end ML pipeline** for personalized nutrition recommendations.  
- Accurately predicts **calories and macronutrient distribution**.  
- Provides **meal and snack counts** tailored to user BMI and fitness goals.  
- Ready-to-deploy ML model (`nutrition_model.pkl`) for integration into applications.  

---

## Future Improvements
- Integrate a **web dashboard** for interactive user input and visualization.  
- Use **advanced ML models** for more accurate predictions.  
- Deploy as a **public web application** using Streamlit.  

---

## Author
**K Oviya**  
Chennai, India  
📧 [k.oviyak9@gmail.com](mailto:k.oviyak9@gmail.com)  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/oviya-k-16a383361)

*Note: I used AI tools to assist with debugging and summarizing this README. All project design, implementation, and code logic were done by me.*
