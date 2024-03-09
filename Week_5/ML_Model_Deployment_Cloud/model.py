import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle


df = pd.read_csv("HR_capstone_dataset.csv")

# Data Processing
df["salary_level"] = df["salary_level"].replace({"low": 0, "medium": 1, "high": 2})
df = pd.get_dummies(df, columns=["Department"], drop_first=True, dtype="uint8")

# Save csv file
df.to_csv("EmployeeDataset.csv")

# dependent and indenpendent 
x = df.drop(columns="has_left_company")
y = df["has_left_company"]

# Split Dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# Train model using best para
best_rf_model = RandomForestClassifier(max_depth=13, n_estimators=122, random_state=1)
best_rf_model.fit(x_train, y_train)

# save model
filename = "RandomForestModel.pkl"
with open(filename, 'wb') as file:
    pickle.dump(best_rf_model, file)


    