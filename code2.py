import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


# 1. Load Data (Using a sample of the Titanic dataset)
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)


# Define features and target
X = data[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']]
y = data['Survived']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 2. Define Preprocessing for Numerical and Categorical Data
# Intermediate Tip: Use ColumnTransformer to handle different types separately
numeric_features = ['Age', 'Fare']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')), # Handle missing values
    ('scaler', StandardScaler())                    # Scale features for better performance
])

categorical_features = ['Pclass', 'Sex', 'Embarked']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore')) # Encode strings to numbers
])


# Combine transformers into a preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])


# 3. Create the Full Pipeline
# This encapsulates the preprocessing AND the model into one object
clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])


# 4. Hyperparameter Tuning with GridSearchCV
# Intermediate Tip: You can tune parameters across the entire pipeline
param_grid = {
    'classifier__n_estimators': [50, 100, 200],
    'classifier__max_depth': [None, 5, 10],
    'preprocessor__num__imputer__strategy': ['mean', 'median']
}


grid_search = GridSearchCV(clf, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)


# 5. Evaluate the Best Model
print(f"Best Parameters: {grid_search.best_params_}")
y_pred = grid_search.predict(X_test)

print("\n--- Classification Report ---")
print(classification_report(y_test, y_pred))





