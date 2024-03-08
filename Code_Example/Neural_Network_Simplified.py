!pip install tensorflow

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

# Load dataset
df = pd.read_csv('path/to/your/dataset.csv')
X = df.drop('price', axis=1)
y = df['price']

# from sklearn.datasets import load_iris
# iris = load_iris()
# X = pd.DataFrame(iris.data, columns=iris.feature_names)
# y = pd.Categorical.from_codes(iris.target, iris.target_names)


######################################################################################################### EDA #########################################################################################################
label_counts = y.value_counts()
missing_percentage = X.isnull().mean() * 100
#or sort it
missing_percentage = X.isnull().mean().round(4).mul(100).sort_values(ascending=False)
X.dtypes
X.info()
X.dtypes.to_dict()

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#######################################################################################################################################################################################################################


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


# Fit the preprocessor to the training data and transform it
X_train_preprocessed = preprocessor.fit_transform(X_train)
y_train_preprocessed = pd.get_dummies(y_train)
# Transform the test data (do not fit the preprocessor to the test data to avoid data leakage)
X_test_preprocessed = preprocessor.transform(X_test)
y_test_preprocessed = pd.get_dummies(y_test)

import tensorflow as tf
from tensorflow.keras import layers

model = tf.keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[X_train_preprocessed.shape[1]]),
    layers.Dense(64, activation='relu'),
    # Adjust the output layer to have 3 neurons (for 3 classes) and use softmax activation for multi-class classification
    layers.Dense(3, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print("X_train_preprocessed shape:", X_train_preprocessed.shape)
print("y_train shape:", y_train.shape)
model.summary()

history = model.fit(X_train_preprocessed, pd.get_dummies(y_train), epochs=100, validation_split=0.2, verbose=0)
#MAKE A MISTAKE HERE
#DEBUGG
#print("X_train_preprocessed shape:", X_train_preprocessed.shape)
#print("y_train shape:", y_train.shape)
#model.summary()

loss, accuracy = model.evaluate(X_test_preprocessed, pd.get_dummies(y_test_preprocessed), verbose=2)
print(f"Test MAE: {loss}, Test MSE: {accuracy}")

predictions = model.predict(X_test_preprocessed)


####################################### Cross Validate ####################

def create_model(input_shape):
    model = tf.keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=[X_train_preprocessed.shape[1]]),
        layers.Dense(64, activation='relu'),
        # Adjust the output layer to have 3 neurons (for 3 classes) and use softmax activation for multi-class classification
        layers.Dense(3, activation='softmax')
    ])
    model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
    return model

from sklearn.model_selection import StratifiedKFold
kf = StratifiedKFold(n_splits=5)  # 5-fold cross-validation
fold_no = 1
for train_index, val_index in kf.split(X, y):
    X_train, X_val = X.iloc[train_index], X.iloc[val_index]
    y_train, y_val = pd.Series(y).iloc[train_index], pd.Series(y).iloc[val_index]
    
    # Fit the preprocessor to the training data and transform it
    X_train_preprocessed = preprocessor.fit_transform(X_train)
    y_train_preprocessed = pd.get_dummies(y_train)
    # Transform the test data (do not fit the preprocessor to the test data to avoid data leakage)
    X_val_preprocessed = preprocessor.transform(X_val)
    y_val_preprocessed = pd.get_dummies(y_val)

    model = create_model(input_shape=[X_train_preprocessed.shape[1]])
    
    print(f'Training on fold {fold_no}...')
    
    # Fit the model
    model.fit(X_train_preprocessed, y_train_preprocessed, epochs=10, batch_size=32, validation_data=(X_val_preprocessed, y_val_preprocessed), verbose=0)
    
    # Optionally, evaluate the model
    scores = model.evaluate(X_val_preprocessed, y_val_preprocessed, verbose=0)
    print(f'Score for fold {fold_no}: {model.metrics_names[0]} of {scores[0]}; {model.metrics_names[1]} of {scores[1]}')
    
    fold_no += 1
