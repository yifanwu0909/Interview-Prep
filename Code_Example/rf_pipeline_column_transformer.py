from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score

label_counts = df['target'].value_counts()
missing_percentage = df.isnull().mean() * 100
#or sort it
missing_percentage = df.isnull().mean().round(4).mul(100).sort_values(ascending=False)
df.dtypes
df.info()
df.dtypes.to_dict()

num_pipeline = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='mean')),
    ('scale', StandardScaler())
])

cat_pipeline = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='constant', fill_value=0)),
    ('encode', OneHotEncoder(handle_unknown='ignore'))
])

num_columns = df.select_dtypes(include=['float', 'int']).columns
cat_columns = df.select_dtypes(include=['object']).column

preprocessor = ColumnTransformer(transformers=[
    ('num', num_pipeline, num_columns),
    ('cat', cat_pipeline, cat_columns),
    ('drop_cat_feature_drop', 'drop', ['cat_feature_drop'])  # Dropping the column
])

# Final pipeline including the classifier
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X_df, y, test_size=0.2, random_state=42)

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
rf_model.fit(X_train, y_train)

# Predict on the test set
y_pred = rf_model.predict(X_test)
###########################################################################################

# Train the model
pipeline.fit(X_train, y_train)

cv_scores = cross_val_score(model_pipeline, X_trainval, y_trainval, cv=5, scoring='accuracy')

# Evaluate the model
print(f"Model accuracy on test set: {pipeline.score(X_test, y_test):.4f}")

# Define Stratified K-Fold cross-validation
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(pipeline, X_trainval, y_trainval, cv=skf, scoring='accuracy')
print("Cross-validation scores:", scores)
print("Mean accuracy:", scores.mean())
print("Standard deviation of accuracy:", scores.std())
