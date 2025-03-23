import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Sample training data (You can replace this with real data)
data = {
    "sales": [50, 40, 70, 60, 55, 45, 30, 80, 90, 20, 100, 35, 65, 85, 75, 95, 25, 15, 110, 120, 
              33, 77, 48, 95, 88, 52, 67, 92, 58, 43, 125, 135, 145, 28, 39, 74, 82, 66, 55, 48, 
              99, 113, 121, 140, 37, 68, 91, 102, 86, 72],
    
    "reviews": [4.5, 4.2, 4.8, 4.6, 4.3, 4.1, 3.9, 4.9, 5.0, 3.5, 4.9, 3.8, 4.7, 4.6, 4.4, 4.5, 3.7, 3.0, 5.0, 4.8, 
                3.6, 4.2, 3.9, 4.7, 4.3, 3.5, 4.1, 4.8, 4.0, 3.8, 5.0, 4.9, 4.7, 3.6, 3.9, 4.5, 4.3, 4.1, 3.7, 
                4.6, 4.8, 5.0, 4.9, 3.5, 4.4, 4.3, 4.7, 4.5, 4.2, 4.6],  # Added one value
    
    "response_time": ["Fast", "Moderate", "Very Fast", "Slow", "Fast", "Moderate", "Slow", "Very Fast", "Very Fast", "Slow",
                      "Fast", "Moderate", "Very Fast", "Fast", "Moderate", "Very Fast", "Slow", "Slow", "Very Fast", "Very Fast", 
                      "Slow", "Fast", "Moderate", "Fast", "Very Fast", "Moderate", "Slow", "Very Fast", "Fast", "Slow", 
                      "Very Fast", "Very Fast", "Very Fast", "Slow", "Moderate", "Fast", "Fast", "Moderate", "Slow", "Slow",
                      "Very Fast", "Very Fast", "Very Fast", "Fast", "Slow", "Moderate", "Slow", "Very Fast", "Fast", "Fast"],

    "rating": [4.8, 4.2, 5.0, 3.8, 4.4, 3.9, 3.5, 5.0, 5.0, 3.0, 5.0, 3.7, 4.9, 4.8, 4.6, 4.7, 3.5, 2.9, 5.0, 5.0, 
               3.2, 4.3, 3.8, 4.9, 4.5, 3.6, 4.2, 4.8, 4.1, 3.7, 5.0, 5.0, 4.9, 3.4, 3.8, 4.6, 4.5, 4.2, 3.6, 
               4.8, 4.9, 5.0, 4.9, 3.5, 4.5, 4.3, 4.8, 4.7, 4.3, 4.6]  # Added one value
}



df = pd.DataFrame(data)

# Encode categorical 'response_time'
encoder = LabelEncoder()
df["response_time_encoded"] = encoder.fit_transform(df["response_time"])

# Features and target variable
X = df[["sales", "reviews", "response_time_encoded"]]
y = df["rating"]

# Train AI model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model and encoder
joblib.dump(model, "rating_model.pkl")
joblib.dump(encoder, "encoder.pkl")

print("AI Model Trained and Saved!")
