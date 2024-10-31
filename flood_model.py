import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
from sklearn.metrics import r2_score

# Load the dataset
data = pd.read_csv("D:/Internship/Day-10-11th July/flood.csv")

# Select the relevant features and target
X = data[['ClimateChange', 'TopographyDrainage', 'DamsQuality', 'MonsoonIntensity']]
y = data['FloodProbability']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred) * 100

# Save the trained model as a pickle file
joblib.dump(model, 'flood_prediction_model.pkl')

print(f"R^2 Score: {r2:.2f}%")
