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
[Back to TOC](#ML-Questions)


## Why Normalization?
[Back to TOC](#ML-Questions)


## Too Many Categories in Categorical Features
[Back to TOC](#ML-Questions)


## Would an Additional Feature Improve GBM or Logistic Regression More?
[Back to TOC](#ML-Questions)


## Feature Engineering
[Back to TOC](#ML-Questions)


## Lasso and Ridge
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


