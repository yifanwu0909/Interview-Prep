!pip install tensorflow

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv('path/to/your/dataset.csv')
X = df.drop('price', axis=1)
y = df['price']

# Load the Iris dataset
# from sklearn.datasets import load_iris
# iris = load_iris()
# X = pd.DataFrame(iris.data, columns=iris.feature_names)
# y = iris.target

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

X = df.drop('price', axis=1)
y = df['price']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

import tensorflow as tf
from tensorflow.keras import layers

# Define the model
model = tf.keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[X_train.shape[1]]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
])

model.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics=['mean_absolute_error', 'mean_squared_error'])

history = model.fit(X_train, y_train, epochs=100, validation_split=0.2, verbose=1)

test_loss, test_mae, test_mse = model.evaluate(X_test, y_test, verbose=2)
print(f"Test MAE: {test_mae}, Test MSE: {test_mse}")

predictions = model.predict(X_test)


####################################### Cross Validate ####################

def create_model(input_shape):
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=input_shape),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)  # Adjust the output layer according to your problem
    ])
    model.compile(optimizer='adam', loss='mean_squared_error') 
    return model

kf = KFold(n_splits=5)  # 5-fold cross-validation
fold_no = 1
for train_index, val_index in kf.split(X):
    X_train, X_val = X[train_index], X[val_index]
    y_train, y_val = y[train_index], y[val_index]

    model = create_model(input_shape=[X_train.shape[1]])
    
    print(f'Training on fold {fold_no}...')
    
    # Fit the model
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))
    
    # Optionally, evaluate the model
    # scores = model.evaluate(X_val, y_val, verbose=0)
    # print(f'Score for fold {fold_no}: {model.metrics_names[0]} of {scores[0]}; {model.metrics_names[1]} of {scores[1]}')
    
    fold_no += 1
