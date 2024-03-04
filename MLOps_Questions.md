# MLOps Questions

- [Model Monitoring](#model-monitoring)   
  - [Cues for Retraining](#cues-for-retraining)   
  - [Error Rate Based Drift Detection](#error-rate-based-drift-detection)   
  - [Drift Detection on the Target Variable](#drift-detection-on-the-target-variable)   
  - [Drift Detection on the Input Data](#drift-detection-on-the-input-data)   
  - [Summary](#summary)   
- [Explain about Model/Concept Drift](#explain-about-model-or-concept-drift)
- [Train/Serve Skew](#train-or-serve-skew)
- [Features of each Cloud MLOps tool](#features-of-each-mlops-tool)
- [How to Create CI/CD Pipelines for Machine Learning](#how-to-create-cicd-pipelines-for-machine-learning)
- [How Would You Scale Your ML Model](#how-would-you-scale-your-ml-model)
- [How to Maintain Model Versioning](#how-to-maintain-model-versioning)
- [What Types of Testing Should Be Carried Out Before Deploying an ML Model into Production?](#what-types-of-testing-should-be-carried-out-before-deploying-an-ml-model-into-production)
- [What Production Testing Techniques Are There?](#what-production-testing-techniques-are-there)
- [What Are the Important Steps That Need to Be Taken Care of After Deployment?](#what-are-the-important-steps-that-need-to-be-taken-care-of-after-deployment)
- [What’s the Difference Between Continuous Integration, Delivery, and Deployment?](#whats-the-difference-between-continuous-integration-delivery-and-deployment)
- [How You Can Update a New Model with Little Downtime](#how-you-can-update-a-new-model-with-little-downtime)
- [Describe Some Common Issues Involved in the Deployment of Machine Learning Models](#describe-some-common-issues-involved-in-the-deployment-of-machine-learning-models)
- [How DevOps and MLOps Are Different](#how-devops-and-mlops-are-different)
- [Stream Processing vs Batch Processing](#stream-processing-vs-batch-processing)
- [How Can We Ensure Reproducibility When Deploying Machine Learning Models?](#how-can-we-ensure-reproducibility-when-deploying-machine-learning-models)
- [What Is the Concept of “Immutable Infrastructure”?](#what-is-the-concept-of-immutable-infrastructure)
- [What Is Your Opinion on the A/B Split Approach to Model Evaluation?](#what-is-your-opinion-on-the-ab-split-approach-to-model-evaluation)
- [Difference Between CMD and Entrypoint](#difference-between-cmd-and-entrypoint)
- [Can There Be Multiple CMD Commands or Entrypoint Command?](#can-there-be-multiple-cmd-commands-or-entrypoint-command)
- [How to Run Multiple RUN Commands in One Line in a Docker File](#how-to-run-multiple-run-commands-in-one-line-in-a-docker-file)
- [Data Archiving](#data-archiving)
- [Data Warehousing](#data-warehousing)
- [What Are the 4 Key Components of a Data Warehouse?](#what-are-the-4-key-components-of-a-data-warehouse)
- [What Are the Steps to Build the Datawarehouse?](#what-are-the-steps-to-build-the-datawarehouse)
- [What Is Real-time Datawarehousing?](#what-is-real-time-datawarehousing)
- [What Is Active Datawarehousing?](#what-is-active-datawarehousing)
- [What Is the Difference Between OLTP and OLAP?](#what-is-the-difference-between-oltp-and-olap)
- [What Is the Difference Between Datawarehouse and OLAP?](#what-is-the-difference-between-datawarehouse-and-olap)

## Model Monitoring
The knowledge embedded in a machine learning model is a frozen snapshot of a real-world process imperfectly captured in data. Even if your machine learning (ML) models aren’t wrong now, drift will inevitably affect any model and cause it to lose accuracy over time. 
A change in any step in the model dependency pipeline may violate the statistical, technical, or business assumptions that were relied upon when the model was built, which will require the model to be retrained. 

![Alt text](Pictures/model_monitoring.png)

[Back to TOC](#MLOps-Questions)    


### Cues for Retraining
we can monitor the input and outputs of our model and trigger model retraining upon the following events: 
- The model’s performance metrics have deteriorated.
- The distribution of predictions has changed from those observed during training. 
- The training data and the live data have begun to diverge and the training data is no longer a good representation of the real world.

Ideally, predictions and the inputs that produced them are logged and easily accessible to facilitate monitoring. The best approach is to tie the model calls to a unique ID which can be used to retrieve the prediction and logging data. If possible, this prediction should either immediately or eventually be tied to a ground truth label. These ground truths are then used to calculate and visualize a performance metric that should be made available to users across the organization. 

[Back to TOC](#MLOps-Questions)    


### Error Rate Based Drift Detection
Detecting drift based on model performance, or “error rate based drift detection,” ties directly to what we care most about — model performance — and is generally simple to implement. In this strategy, when we observe a significant dip in model performance, we retrain our model. The threshold for retraining should be determined based on the performance expectations set during model development. 

[Back to TOC](#MLOps-Questions)    


### Drift Detection on the Target Variable
Even without available labels, we can still monitor the distribution of predictions and compare it to the distribution of predictions that we observed over the training data. Prediction data for many use cases tend to be univariate or low dimensional, making some of the common methods for comparing distributions easier to implement and interpret. Some of the more common statistical tests used to compare distributions are the Z-test, Chi-squared, Kolmogorov–Smirnov, Jensen-Shannon, and Earth Mover’s Distance. No matter the chosen metric (similar to error rate-based drift detection) you’ll need to determine a threshold for when retraining becomes necessary.

![Alt text](Pictures/drift.png)

[Back to TOC](#MLOps-Questions)    


### Drift Detection on the Input Data
we could generate baseline statistics from our training data for each feature and compare these statistics to those seen in the live data. Alternatively (or additionally), we can train a binary classifier to distinguish between training data and live data. Being able to distinguish between the training data and live data (a better-than-random AUC) suggests that the data has drifted.

[Back to TOC](#MLOps-Questions)    


### Summary
- Trace and understand the dependencies of your model.
- Select a drift detection method that’s appropriate for your model and data:
	- Error rate
	- Target variable
	- Input data
- Select a metric and threshold for retraining.
- When the threshold has been crossed:
	- Perform error analysis and debug model dependencies for insights
	- Retrain your model 
- Iterate and improve.
  
[Back to TOC](#MLOps-Questions)    


## Explain about Model or Concept Drift
Model drift, sometimes called concept drift, occurs when the model performance during the inference phase (using real-world data) degrades when compared to its performance during the training phase (using historical, labeled data). It is also known as train/serve skew as the performance of the model is skewed when compared with the training and serving phases. This could be due to many reasons like
- The underlying distribution of data has changed
- Unforeseen events - like a model trained on pre-covid data is expected to perform much worse on data during the COVID-19 pandemic
- Training happened on a limited number of categories but a recent environmental change happened which added another category
- In NLP problems the real world data has significantly more number of tokens that are different from training data
To detect model drift, it is always necessary to keep continuously monitoring the performance of the model. If there is a sustained degradation of model performance, the cause needs to be investigated and treatment methods need to be applied accordingly which almost always involves model retraining.

[Back to TOC](#MLOps-Questions)    


## Train or Serve Skew
The challenge is that all the processing steps need to be repeated when trying to derive inferences because the model expects the data on which predictions need to be issued to be in the same format as the training data.
If the prediction data differs significantly from the training data then it can be argued that there is a train/serve skew.
There are multiple ways to avoid train serve skew like:
- Maintain separate module files for data preprocessing (a separate class or module.py file)
- Compose a preprocessing graph using TFX transform graph etc
  
[Back to TOC](#MLOps-Questions)    


## Features of each MLOps tool

[Source](https://neptune.ai/blog/packaging-ml-models#:~:text=ML%20packing%20tools%20were%20created,track%20of%20this%20for%20you.)

| MLOps Features | MLFlow | Google Kubeflow | TensorFlow Lite & TensorFlow Extended | Azure Machine Learning | AWS SageMaker |
|----------------|--------|-----------------|----------------------------------------|------------------------|---------------|
| Data and Pipeline Versioning | No | Yes | Yes | Yes | Yes |
| Run Orchestration | Limited | Yes | Yes | Yes | Yes |
| Model and Experiment Versioning | Yes | Yes | Using Machine Learning Metadata (MLMD) | Yes | Yes |
| Hyperparameter Tuning / Optimization | Yes | Yes | Yes | Yes | Yes |
| Model Serving | Yes | Yes | Yes | Limited | Limited |
| Model Deployment and Monitoring in Production / Experiment Tracking | Yes | Yes | Yes | Yes | Yes |

| MLOps Features | MLFlow | Google Kubeflow | TensorFlow Lite & TensorFlow Extended | Azure Machine Learning | AWS SageMaker |
|----------------|--------|-----------------|----------------------------------------|------------------------|---------------|
| Open Source / Cloud | Open Source | Open Source | Open Source | Cloud | Cloud |
| Deployment On Premise | Yes | Yes | Yes | No | No |
| Experiment Data Storage | Local + Cloud | Cloud | Local | Cloud | Cloud |
| Easy Setup & Integration | Yes | No | Yes | Yes | Yes |
| Scalable for Large No. of Experiments | Yes | Yes | No | Yes | Yes |
| Custom Visualizations | Yes | Yes | Yes | Yes | Yes |

[Back to TOC](#MLOps-Questions)    


## How to Create CI/CD Pipelines for Machine Learning
[Back to TOC](#MLOps-Questions)    


## How Would You Scale Your ML Model
[Back to TOC](#MLOps-Questions)    


## How to Maintain Model Versioning
[Back to TOC](#MLOps-Questions)    


## What Types of Testing Should Be Carried Out Before Deploying an ML Model into Production?
[Back to TOC](#MLOps-Questions)    


## What Production Testing Techniques Are There?
[Back to TOC](#MLOps-Questions)    


## What Are the Important Steps That Need to Be Taken Care of After Deployment?
[Back to TOC](#MLOps-Questions)    


## What’s the Difference Between Continuous Integration, Delivery, and Deployment?
[Back to TOC](#MLOps-Questions)    


## How You Can Update a New Model with Little Downtime
[Back to TOC](#MLOps-Questions)    


## Describe Some Common Issues Involved in the Deployment of Machine Learning Models
[Back to TOC](#MLOps-Questions)    


## How DevOps and MLOps Are Different
[Back to TOC](#MLOps-Questions)    


## Stream Processing vs Batch Processing
[Back to TOC](#MLOps-Questions)    


## How Can We Ensure Reproducibility When Deploying Machine Learning Models?
[Back to TOC](#MLOps-Questions)    


## What Is the Concept of “Immutable Infrastructure”?
[Back to TOC](#MLOps-Questions)    


## What Is Your Opinion on the A/B Split Approach to Model Evaluation?
[Back to TOC](#MLOps-Questions)    


## Difference Between CMD and Entrypoint
[Back to TOC](#MLOps-Questions)    


## Can There Be Multiple CMD Commands or Entrypoint Command?
[Back to TOC](#MLOps-Questions)    


## How to Run Multiple RUN Commands in One Line in a Docker File
[Back to TOC](#MLOps-Questions)    


## Data Archiving
[Back to TOC](#MLOps-Questions)    


## Data Warehousing
[Back to TOC](#MLOps-Questions)    


## What Are the 4 Key Components of a Data Warehouse?
[Back to TOC](#MLOps-Questions)    


## What Are the Steps to Build the Datawarehouse?
[Back to TOC](#MLOps-Questions)    


## What Is Real-time Datawarehousing?
[Back to TOC](#MLOps-Questions)    


## What Is Active Datawarehousing?
[Back to TOC](#MLOps-Questions)    


## What Is the Difference Between OLTP and OLAP?
[Back to TOC](#MLOps-Questions)    


## What Is the Difference Between Datawarehouse and OLAP?
[Back to TOC](#MLOps-Questions)    

