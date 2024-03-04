# ML Questions

1. [Bias & Variance Trade Off](#bias--variance-trade-off)
   - [Definition](#definition)
   - [Bias](#bias)
   - [Variance](#variance)
2. [Techniques for Reducing Variance](#techniques-for-reducing-variance)
3. [Techniques for Reducing Bias](#techniques-for-reducing-bias)
4. [Data Cleaning](#data-cleaning)
5. [Handle Missing Data](#handle-missing-data)
6. [Label Imbalance](#label-imbalance)
7. [How to Feature Selection](#how-to-feature-selection)
8. [Procedure for Hyperparameter Tuning](#procedure-for-hyperparameter-tuning)
9. [Improve Poor Model Performance](#improve-poor-model-performance)
10. [Bagging vs Boosting](#bagging-vs-boosting)
11. [How does one Collect Data and Prepare Dataset for Training?](#how-does-one-collect-data-and-prepare-dataset-for-training)
12. [Why Normalization?](#why-normalization)
13. [Too Many Categories in Categorical Features](#too-many-categories-in-categorical-features)
14. [Would an Additional Feature Improve GBM or Logistic Regression More?](#would-an-additional-feature-improve-gbm-or-logistic-regression-more)
15. [Feature Engineering](#feature-engineering)
16. [Lasso and Ridge](#lasso-and-ridge)
17. [AUC and ROC](#auc-and-roc)
18. [What is the Intuition Behind the F1 Score?](#what-is-the-intuition-behind-the-f1-score)
19. [How would you Build a Bank Fraud Detection Model?](#how-would-you-build-a-bank-fraud-detection-model)
20. [CNN](#cnn)
    - [Convolution Layer](#convolution-layer)
    - [Pooling Layer](#pooling-layer)
    - [Fully Connected Layer](#fully-connected-layer)
    - [Non-Linearity Layers](#non-linearity-layers)
21. [Vanishing Gradient](#vanishing-gradient)
22. [Exploding Gradient](#exploding-gradient)
23. [Resnet](#resnet)
24. [MobileNet](#mobilenet)
25. [Keras vs Tensorflow vs Pytorch](#keras-vs-tensorflow-vs-pytorch)
26. [Unreasonable Effectiveness of Data](#unreasonable-effectiveness-of-data)
27. [Difference between Xgboost and Random Forest](#difference-between-xgboost-and-random-forest)
28. [Random Forest VS Decision Tree](#random-forest-vs-decision-tree)
29. [How to Prune Decision Tree](#how-to-prune-decision-tree)
30. [Data Science Behavioral Question](#data-science-behavioral-question)


## Bias & Variance Trade Off
### Definition
Of the changes you could make to most learning algorithms, there are some that reduce bias errors but at the cost of increasing variance, and vice versa.
### Bias
An error that occurs due to overly simplistic assumptions or erroneous assumptions in the learning algorithm. If you use bias, it can lead to the model underfitting your data with low predictive accuracy.
### Variance
An error due to complexity in the learning algorithm. In variance, your data gets highly sensitive to high degrees of variation, leading your model to overfit the data. You'll end up carrying noise from your training data for your model to be useful for your test data. 

[Back to TOC](#ML-Questions)

## Techniques for Reducing Variance
1. Add more data
2. Add penalties(L1 and L2)
3. Early stopping and drop out
4. Feature selection 
5. Decrease model size
6. Modify input features based on insights from error analysis
7. Modify model architecture

[Back to TOC](#ML-Questions)


## Techniques for Reducing Bias
1. Increase the model size
2. Modify input features based on insights from error analysis (boosting)
3. Reduce/eliminate regularization
4. Modify model architecture
   
[Back to TOC](#ML-Questions)


## Data Cleaning
2. Remove irrelevant data
3. Standardize capitalization
4. Convert data type
5. Clear formatting
6. Fix errors
7. Language translation
8. Handle missing values
   
[Back to TOC](#ML-Questions)


## Handle Missing Data
Three types of missing data values:
1. Missing Completely at Random: No pattern to the missing data.
2. Missing at Random (MAR): Missing data can be explained by other data in the dataset.
3. Missing Not at Random (MNAR): Missing value is related to the value itself.

Three strategies for handling missing data:
1. **Deleting Rows**: Removing rows with missing values, which can lead to loss of information.   
2. **Imputing Data**: Filling in missing data based on information in the column or other columns in the dataset.
3. **Using Classification or Regression Models**: Predicting missing values using models.

[Back to TOC](#ML-Questions)


## Label Imbalance
1. **Resampling**:
	- Down-sampling the majority class:  model converge faster. However, lead to losing potentially important data.
	- Over-sampling the minority class: better representation of the minority class.
2. **Synthetic data generation**:ing techniques like the Synthetic Minority Over-sampling Technique (SMOTE).
3. **Cost-sensitive learning**: Assigning different weights to samples from different classes to account for the imbalance in the loss function used to train the model.
4. **Ensemble methods**: trained on different subsets of the data with boosting or bagging.
5. **Precision-oriented modeling**: Some models are better suited for evaluation metrics sensitive to imbalanced datasets, such as precision. For example, in decision trees and their variants – like random forest, boosted trees, etc. – one can prune paths with high entropy or with sparse samples. Alternatively, models that generate probability-based outputs, such as logistic regression, can be thresholdedto attain the desired performance outcomes.
**Insider Tip**:  particularly with large capacity models, best to do nothing.

[Back to TOC](#ML-Questions)


## How to Feature Selection
1. **Filter**:  statistical tests such as ANOVA, mutual information, information gain, chi-squared test, correlation coefficient, and others.
2. **Business Insight**
3. **Algorithmic**: the Random Forest method can do feature importance. An alternative approach incorporates L1 regularization, shrink less informative features weight to 0.

[Back to TOC](#ML-Questions)


## Procedure for Hyperparameter Tuning
In **grid search**, a predefined set of hyperparameters are evaluated exhaustively, while in random search, hyperparameters are selected randomly from a predefined search space. These approaches can be inefficient, especially for models that have a large number of hyperparameters or ones that take a long time to train.

**Bayesian optimization** leverages a probabilistic model to approximate the relationship between hyperparameters and the model performance, using an acquisition function that guides the search by balancing exploration (sampling new hyperparameters) and exploitation (evaluating promising hyperparameters).

In a **genetic algorithm**, models represent combinations of hyperparameters ("genes"). The process involves selecting the fittest models from each generation in an iterative manner. The surviving models undergo modification ("mutation") or recombination ("crossover") of their hyperparameters.
Bayesian optimization and genetic algorithms can be effective in finding hyperparameter values for complex models and large datasets.

[Back to TOC](#ML-Questions)


## Improve Poor Model Performance
1. **Overfitting or underfitting?**
2. **Define the problem**: Clearly define what is considered as "poor performance". Is the model compiling? Are there runtime issues? Is the loss not converging, or simply too high? Are model predictions outside of expected bounds?
3. **Visualize the data**: Plot the data to check for patterns, outliers, corruption. Determine whether the dataset is being sampled properly, or if there are any ingestion issues. Check the data before and after preprocessing. For instance, missing values might be too pervasive, handled incorrectly, or numerical features are not properly normalized.
4. **Step through the model**: Inspect the model state at each layer for several steps. Print the outputs of all tensor operations, including outputs of activation functions. It is common to discover problems such as incorrect tensor operations, outliers, NaNs, and improper inputs at this stage.
5. **Loss**: Verify the loss computation is correct. Check the learning rate, gradient computation, and layer weights. After several steps, verify optimizer behaviors like momentum.
6. **Simplify the model**: If model performance is still difficult to troubleshoot, simplify all components of the model. Ingest fewer layers, and use a simple optimizer like SGD. Use fewer parameters, ensure the optimizer converges. Once the model is converging and metrics are moving in the right direction, incrementally add complexity back and verify once more.
7. **Debugging with TensorBoard**: Use TensorBoard to visualize the training process, such as loss over time, to help identify issues with the model. For instance, if the model shows signs of overfitting, apply regularization or early stopping.
8. **Model tuning**: To get better performance, experiment with various components of the model:
	- Feature selection
	- Feature preprocessing
	- Layers
	- Training label
	- Loss function
Further considerations include layer activations, hyperparameters, and model architecture.

[Back to TOC](#ML-Questions)


## Bagging vs Boosting

Bagging and Boosting are both ensemble techniques in machine learning, where multiple models (often of the same type) are trained to solve the same problem and combined to get better results. The key idea behind these methods is that a group of weak learners can come together to form a strong learner. Despite their similarities, they have distinct differences in how they approach building the ensemble of models.

### Bagging (Bootstrap Aggregating)

**Key Concepts:**
- **Parallel Ensemble**: Each model in the ensemble votes independently, and their predictions are combined through averaging (for regression) or majority voting (for classification).
- **Bootstrap Sampling**: Creates different training datasets by randomly sampling with replacement from the original dataset. Each model gets a slightly different dataset, which helps in reducing variance.
- **Equal Weighting**: Each model in the ensemble has an equal vote on the final outcome.

**Objective**: Primarily aims to reduce variance and overfitting in complex models.

**Example**: **Random Forest** is a popular bagging ensemble method that uses multiple decision trees.

### Boosting

**Key Concepts:**
- **Sequential Ensemble**: Models are added sequentially to correct the errors made by previous models. Later models focus more on the data points that were misclassified or had a higher error by earlier models.
- **Weighted Data Points**: Misclassified or harder to predict data points are given more weight, so subsequent models focus more on them.
- **Weighted Voting**: The final prediction is made based on a weighted vote, where more accurate models have more influence.

**Objective**: Aims to reduce both bias and variance by focusing on reducing errors from previous models, making it powerful but also prone to overfitting if not carefully tuned.

**Example**: AdaBoost (Adaptive Boosting) and Gradient Boosting are well-known boosting methods.

### Comparison

| Feature | Bagging | Boosting |
|---------|---------|----------|
| **Model Building** | Models are built independently. | Models are built sequentially to correct the predecessors' errors. |
| **Sampling Method** | Uses bootstrap sampling to create different training datasets. | Reweights the data to focus on more difficult cases. |
| **Decision Making** | Takes an equally weighted average or majority vote of its models. | Uses a weighted average or vote, giving more influence to better-performing models. |
| **Objective** | Aims to reduce variance and avoid overfitting, suitable for high-variance, low-bias models. | Aims to reduce both bias and variance but may increase the risk of overfitting. |
| **Example Methods** | Random Forest. | AdaBoost, Gradient Boosting. |

If the problem is that the single model gets a very low performance, Bagging will rarely get a better bias. However, Boosting could generate a combined model with lower errors as it optimises the advantages and reduces pitfalls of the single model.
By contrast, if the difficulty of the single model is over-fitting, then Bagging is the best option. Boosting for its part doesn’t help to avoid over-fitting; in fact, this technique is faced with this problem itself. For this reason, Bagging is effective more often than Boosting.

| Similarities | Differences |
|--------------|-------------|
| Both are ensemble methods to get N learners from 1 learner | … but, while they are built independently for Bagging, Boosting tries to add new models that do well where previous models fail. |
| Both generate several training data sets by random sampling | … but only Boosting determines weights for the data to tip the scales in favor of the most difficult cases. |
| Both make the final decision by averaging the N learners (or taking the majority of them) | … but it is an equally weighted average for Bagging and a weighted average for Boosting, more weight to those with better performance on training data. |
| Both are good at reducing variance and provide higher stability | … but only Boosting tries to reduce bias. On the other hand, Bagging may solve the over-fitting problem, while Boosting can increase it. |

[Back to TOC](#ML-Questions)


## How does one Collect Data and Prepare Dataset for Training?
1. Collect data: sampling technique random shuffle
2. Clean: missing or duplication, outlier, noise. 
3. Label: human annotators or historic data
4. Split: train and test 
5. Feature engineering on train first and then apply the same logic to test to prevent data leak. Check for data imbalance
6. Shuffle and train

[Back to TOC](#ML-Questions)


## Why Normalization?
Bring all the features to a similar scale, so no single feature dominates the learning process.

1. **Faster Convergence**: The optimizer doesn't have to deal with differing scales for different features.
2. **Stabilize Gradient Steps**: Helps in stabilizing the gradient descent steps.
3. **Equal Importance**: Ensures that all features have equal importance in the learning process.
4. **Improved Performance**: Some algorithms, such as k-Nearest Neighbors and neural networks, are sensitive to the scale of the features.
5. **Requirement for Some Algorithms**: Certain machine learning algorithms, such as Support Vector Machines and Principal Component Analysis, require normalization to function correctly.
   
[Back to TOC](#ML-Questions)


## Too Many Categories in Categorical Features
### Approach1: Use domain knowledge:
1. Decrease the number of groups and apply one-hot encoding: Think of the meaningful ways to map your data to several larger categories. Then one-hot encode.
2. Quantitative mapping: designate each category with a score or statistic.
### Approach2: Learn from the output variable
1. Calculate aggregated value per group
	- classifier: ratio of positive labels / group
	- regression: mean target value / group
2. Calculate normalized aggregated value per group: weight of evidence score & Perlich aggregations
   
[Back to TOC](#ML-Questions)


## Would an Additional Feature Improve GBM or Logistic Regression More?
Too many features causes overfitting problems:
1. **Curse of Dimensionality**: Too many features result in the Curse of dimensionality.
2. **Sparse Data**: Curse of dimensionality results in data being sparse (especially if datapoints are too few).
3. **Model Overfitting**: Data being sparse results in model overfitting.

As we add more features, the available data points in our feature space become exponentially sparser, which makes it easier to separate the data points. Yet, it’s not because of any pattern in the data, in actuality it’s just the nature of higher dimensional spaces. Because of this inherent sparsity, we end up overfitting when we add more features to our data. This means we need more data to avoid sparsity — and that’s the curse of dimensionality: as the number of features increase, our data become sparser, which results in overfitting, and we therefore need more data to avoid it.

[Back to TOC](#ML-Questions)


## Feature Engineering
### Def
the act of converting raw observations into desired features using statistical or machine learning approaches. Feature engineering is a machine learning technique that leverages data to create new variables that aren’t in the training set. It can produce new features for both supervised and unsupervised learning, with the goal of simplifying and speeding up data transformations while also enhancing model accuracy.
### Importance
1. **Enhanced Predictive Power**: helps models to better capture the underlying patterns and relationships, improving their predictive accuracy.
2. **Noise Reduction**: filter out irrelevant noise.
3. **Revealing Subtle Patterns**: The process can uncover subtle patterns that might be hidden in the raw data.
4. **Task-Specific Customization**: tailors features to the specific needs of the modeling task, ensuring that the input data is optimally suited for the problem at hand.
5. **Capturing Non-Linear Relationships**: Engineered features can reveal non-linear relationships that simpler, linear models might miss, thereby enhancing model complexity and adaptability.
6. **Model Resilience**: Features that are well-engineered contribute to a model's robustness, helping it to maintain performance even as data distributions change over time.
7. **Domain Expertise Integration**: Incorporating domain knowledge into feature engineering can capture important nuances that raw data might not reflect, aligning the features more closely with the problem domain.
8. **Dimensionality Reduction**: Thoughtful feature engineering can reduce the number of input features, which simplifies the model and reduces computational costs.
9. **Improved Interpretability**: By encapsulating meaningful insights, engineered features can make models more interpretable and understandable to stakeholders.
### Techniques
1. **Imputation**:
   - Handle missing values in your dataset.
   - Replace missing values with the mean, median, mode, or use more advanced imputation techniques like K-Nearest Neighbors (KNN) or regression imputation.
2. **One-Hot Encoding**:
   - Convert categorical variables into a binary matrix.
   - Use tools like `pandas.get_dummies()` in Python or `OneHotEncoder` from scikit-learn.
3. **Label Encoding**:
   - Convert categorical labels into numerical values.
   - Use `LabelEncoder` from scikit-learn.
4. **Target Encoding**:
   - Encode categorical features based on the mean of the target variable for each category.
   - Implement target encoding manually or use libraries like `category_encoders` in Python.
5. **Frequency Encoding**:
   - Encoding categorical variables based on their frequency or occurrence in the dataset.
6. **Cyclical Encoding**:
   - Encoding cyclical features, such as time or angles, using sine and cosine transformations.
7. **Binning or Discretization**:
   - Convert numerical variables into categorical ones by grouping them into bins or intervals.
   - Use `pandas.cut()` or `pandas.qcut()` for equal width or quantile binning, respectively.
8. **Scaling**:
   - Standardize or normalize numerical features to ensure they have similar scales.
   - Use `StandardScaler` or `MinMaxScaler` from scikit-learn.
9. **Log Transform**:
   - Apply the logarithm transformation to skewed numerical features to make their distribution more normal.
   - Use `numpy.log()`.
10. **Aggregation**:
    - Creating aggregated features by summarizing or aggregating information across groups or categories.
11. **Outlier Handling**:
    - Identifying and handling outliers by transforming or capping extreme values.
12. **Cumulative Features**:
    - Creating features that represent cumulative sums or averages over time or within specific groups.
13. **Hashing**:
    - Hashing categorical variables to generate fixed-size representations, useful for high-cardinality features.
14. **Embeddings**:
    - Representing categorical variables using embeddings, which capture relationships between categories.
15. **Cross-Validation Features**:
    - Creating features based on cross-validation folds, such as mean or standard deviation of predictions.
16. **Cluster Labels**:
    - Assigning cluster labels to data points based on clustering algorithms, creating new categorical features.
17. **Feature Splitting**:
    - Splitting combined features or extracting information from them to create new features.
18. **Feature Extraction**:
    - Reduce dimensionality by extracting important features.
    - Principal Component Analysis (PCA), Linear Discriminant Analysis (LDA), or feature selection methods like Recursive Feature Elimination (RFE).
19. **Interaction Terms**:
    - Create new features by combining existing ones.
    - Sum, difference, product, or ratio of two variables.
20. **Polynomial Features**:
    - Generate polynomial features to capture non-linear relationships.
    - Use `PolynomialFeatures` from scikit-learn.
21. **Time-Based Features**:
    - Extract features related to time, such as day of the week, month, or season.
    - Use functions like `datetime` in Python to extract relevant information.
    - Roll-over time series 
22. **Text Processing**:
    - Convert text data into numerical features.
    - Use methods like Bag of Words, TF-IDF, or Word Embeddings
23. **Date and Time Features**:
    - Extracting relevant information from date and time data, such as day of the week, month, or time differences.
24. **Handling Skewed Data**:
    - Address skewness in numerical features.
    - Apply transformations like Box-Cox or Yeo-Johnson.
25. **Custom Transformations**:
    - Assume you want to create a custom transformation function.
### Challenges and Considerations
#### 1. Overfitting
- **Risk**: Complex features may capture noise, leading to overfitting.
- **Strategies**:
  - Focus on features that improve model understanding and predictive power.
  - Use validation sets to monitor overfitting.
  - Prefer simple features for better generalization.
  - Apply regularization and cross-validation.
  - Consult domain experts for feature relevance.
#### 2. Computational Cost
- **Challenge**: Some techniques are computationally intensive, especially on large datasets.
- **Solutions**:
  - Explore parallelization to manage computational load.
  - Apply feature engineering incrementally.
  - Use representative samples for large datasets.
  - Choose efficient algorithms.
  - Monitor and optimize resource usage.
#### 3. Data Leakage
- **Issue**: Information from the testing set influencing model training.
- **Prevention**:
  - Ensure feature engineering is confined to the training phase.
  - Simulate real-world scenarios by not using future information.
  - Be cautious with features derived from the target variable.
  - Implement feature engineering within cross-validation folds.
  - Evaluate model on the testing set post-feature engineering.
  - Maintain transparent documentation to avoid and identify leakage.

[Machine Learning: 14 Feature Engineering Techniques](https://baotramduong.medium.com/machine-learning-14-feature-engineering-techniques-f97040e4f5b5)

[Back to TOC](#ML-Questions)


## Lasso and Ridge
Techniques used to prevent overfitting in regression models by adding a regularization term to the cost function. 

| Feature | Lasso Regression (L1 Regularization) | Ridge Regression (L2 Regularization) |
|---------|--------------------------------------|--------------------------------------|
| **Definition** | Adds a penalty equal to the absolute value of the magnitude of coefficients. | Adds a penalty equal to the square of the magnitude of coefficients. |
| **Key Features** | - Shrink some coefficients to zero for variable selection.<br>- Useful with many features, some irrelevant.<br>- Leads to sparse models. | - Shrinks coefficients evenly but not to zero.<br>- Useful for multicollinearity.<br>- Keeps all features, minimizing impact. |
| **Limitations** | - Struggles with multicollinearity.<br>- Inconsistent when selecting more features than observations. | - Does not perform variable selection.<br>- Can result in complex models due to inclusion of all variables. |
| **Variable Selection** | Can zero out coefficients, performing variable selection. | Only shrinks coefficients close to zero, does not perform variable selection. |
| **Interpretability** | May yield more interpretable models due to variable selection. | Might be less interpretable as it includes all features. |
| **Multicollinearity** | Can struggle with multicollinearity. | Handles multicollinearity better by distributing coefficients among correlated predictors. |
| **Model Complexity** | Can produce simpler models by excluding irrelevant features. | Tends to include all features, which might not be ideal for model simplicity. |
| **Choosing Between Lasso and Ridge** | More appropriate if feature selection is important or if the number of observations is much larger than the number of features. | Preferable when dealing with highly correlated data and interpretability is not a major concern. |

[Back to TOC](#ML-Questions)
### Lasso Regression (L1 Regularization)

**Mathematical Representation**:
```
Cost function = RSS + λ ∑|β_j|
```
### Ridge Regression (L2 Regularization)

**Mathematical Representation**:
```
Cost function = RSS + λ ∑(β_j)^2
```
### Comparison and Choice

- **Variable Selection**: Lasso can zero out coefficients, performing variable selection, while Ridge only shrinks coefficients close to zero.
- **Interpretability**: Lasso may yield more interpretable models due to variable selection. Ridge regression might be less interpretable as it includes all features.
- **Multicollinearity**: Ridge regression handles multicollinearity better than Lasso by distributing coefficients among correlated predictors.
- **Model Complexity**: Lasso can produce simpler models by excluding irrelevant features. Ridge tends to include all features, which might not be ideal for model simplicity.

**Choosing Between Lasso and Ridge**:
- If feature selection is important or if the number of observations is much larger than the number of features, Lasso might be more appropriate.
- If dealing with highly correlated data and interpretability is not a major concern, Ridge might be preferable.
- Elastic Net is a middle ground that combines Lasso and Ridge, potentially offering the best of both worlds when tuning its parameters correctly.



[Back to TOC](#ML-Questions)


## AUC and ROC
[Back to TOC](#ML-Questions)


## What is the Intuition Behind the F1 Score?
[Back to TOC](#ML-Questions)


## How would you Build a Bank Fraud Detection Model?
[Back to TOC](#ML-Questions)


## CNN
### Convolution Layer
### Pooling Layer
### Fully Connected Layer
### Non-Linearity Layers
[Back to TOC](#ML-Questions)


## Vanishing Gradient
[Back to TOC](#ML-Questions)


## Exploding Gradient
[Back to TOC](#ML-Questions)


## Resnet
[Back to TOC](#ML-Questions)


## MobileNet
[Back to TOC](#ML-Questions)


## Keras vs Tensorflow vs Pytorch
[Back to TOC](#ML-Questions)


## Unreasonable Effectiveness of Data
[Back to TOC](#ML-Questions)


## Difference between Xgboost and Random Forest
[Back to TOC](#ML-Questions)


## Random Forest VS Decision Tree
[Back to TOC](#ML-Questions)


## How to Prune Decision Tree
[Back to TOC](#ML-Questions)


## Data Science Behavioral Question
[Back to TOC](#ML-Questions)


