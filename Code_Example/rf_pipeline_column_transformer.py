from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
import pandas as pd


# Load dataset
df = pd.read_csv('path/to/your/dataset.csv')
X = df.drop('price', axis=1)
y = df['price']

# Load the Iris dataset
# from sklearn.datasets import load_iris
# iris = load_iris()
# X = pd.DataFrame(iris.data, columns=iris.feature_names)
# y = pd.Categorical.from_codes(iris.target, iris.target_names)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

label_counts = y.value_counts()
missing_percentage = X.isnull().mean() * 100
#or sort it
missing_percentage = X.isnull().mean().round(4).mul(100).sort_values(ascending=False)
X.dtypes
X.info()
X.dtypes.to_dict()

num_pipeline = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='mean')),
    ('scale', StandardScaler())
])

cat_pipeline = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='constant', fill_value=0)),
    ('encode', OneHotEncoder(handle_unknown='ignore'))
])

num_columns = X.select_dtypes(include=['float', 'int']).columns
cat_columns = X.select_dtypes(include=['object']).columns

preprocessor = ColumnTransformer(transformers=[
    ('num', num_pipeline, num_columns),
    ('cat', cat_pipeline, cat_columns),
    ('drop_cat_feature_drop', 'drop', ['sepal length (cm)'])  # Dropping the column
])

# Final pipeline including the classifier
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])


# Train the model
pipeline.fit(X_train, y_train)
# Evaluate the model
print(f"Model accuracy on test set: {pipeline.score(X_test, y_test):.4f}")
# Define Stratified K-Fold cross-validation
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(pipeline, X_train, y_train, cv=skf, scoring='accuracy')

print("Cross-validation scores:", scores)
print("Mean accuracy:", scores.mean())
print("Standard deviation of accuracy:", scores.std())

######################################### Bagging #########################################
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

# Initialize the base estimator
base_estimator = DecisionTreeClassifier(max_features='sqrt', random_state=42)

# Initialize the Bagging classifier with decision trees as base estimators
# n_estimators: Number of trees in the forest
# max_samples: The fraction of samples to draw from X to train each base estimator
rf_model = BaggingClassifier(base_estimator=base_estimator,
                             n_estimators=100,
                             max_samples=0.8,
                             bootstrap=True,
                             random_state=42)

# Final pipeline including the classifier
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', rf_model)
])

# Train the model
pipeline.fit(X_train, y_train)

# Predict on the test set
y_pred = pipeline.predict(X_test)
# Evaluate the model
print(f"Model accuracy on test set: {pipeline.score(X_test, y_test):.4f}")

# Define Stratified K-Fold cross-validation
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(pipeline, X_train, y_train, cv=skf, scoring='accuracy')

print("Cross-validation scores:", scores)
print("Mean accuracy:", scores.mean())
print("Standard deviation of accuracy:", scores.std())
###########################################################################################



