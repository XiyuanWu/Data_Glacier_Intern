from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    # Render the home page with the input form
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Retrieve and convert form inputs
    try:
        form_data = request.form
        satisfaction_level = float(form_data["satisfaction_level"])
        last_performance_rating = float(form_data["last_performance_rating"])
        number_of_projects = int(form_data["number_of_projects"])
        avg_monthly_hours = int(form_data["avg_monthly_hours"])
        years_at_company = int(form_data["years_at_company"])
        had_work_accident = int(form_data["had_work_accident"])
        promoted_in_last_5_years = int(form_data["promoted_in_last_5_years"])
        department = form_data["Department"]  # Assuming exact matching from form to dataset encoding
        salary_level = form_data["salary_level"]

        # Map salary level from text to numeric
        salary_mapping = {"low": 0, "medium": 1, "high": 2}
        numeric_salary = salary_mapping[salary_level]

        # Encode department - Example placeholder function
        department_encoded = encode_department(department)  # Placeholder for actual encoding logic

        # Prepare model input with correct order and encoding
        input_features = [satisfaction_level, last_performance_rating, number_of_projects,
                          avg_monthly_hours, years_at_company, had_work_accident,
                          promoted_in_last_5_years] + department_encoded + [numeric_salary]

        input_features = np.array(input_features).reshape(1, -1)

        # Predict using the model
        prediction = model.predict(input_features)

        # Interpret the prediction result
        prediction_text = "likely to leave" if prediction[0] == 1 else "likely to stay"

        return render_template("index.html", prediction_text=f"The employee is {prediction_text}.")
    
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error in processing prediction: {e}")

def encode_department(department):

    departments = ["RandD", "accounting", "hr", "management", "marketing", "product_mng", "sales", "support", "technical"]
    encoded = [0] * len(departments)  # Initialize all to 0
    if department in departments:
        encoded[departments.index(department)] = 1  # Set to 1 for the matching department
    return encoded

if __name__ == "__main__":
    app.run(debug=True)
