import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("data/manufacturing_dataset_1000_samples.csv")

# ----- FIX: Handle missing values -----
# Fill numeric missing values with mean
df = df.fillna(df.mean(numeric_only=True))

# Fill text missing values with "Unknown"
df = df.fillna("Unknown")
# --------------------------------------

# Separate input and output
y = df["Parts_Per_Hour"]
X = df.drop("Parts_Per_Hour", axis=1)

# Convert text columns to numbers
X = pd.get_dummies(X)

# Save column names
joblib.dump(X.columns, "model/columns.pkl")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model/manufacturing_model.pkl")

print("Model trained and saved successfully!")
