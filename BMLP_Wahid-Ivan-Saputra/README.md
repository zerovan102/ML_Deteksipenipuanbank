<h1 align="center">💳 Bank Fraud Detection AI Pipeline</h1>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white" alt="Python Version"/>
  <img src="https://img.shields.io/badge/scikit--learn-1.4+-orange?logo=scikit-learn&logoColor=white" alt="Scikit-Learn"/>
  <img src="https://img.shields.io/badge/Pandas-Data_Engineering-purple?logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/FastAPI-Web_App_Ready-009688?logo=fastapi&logoColor=white" alt="FastAPI"/>
</div>

<p align="center">
  <strong>An Advanced End-to-End Machine Learning Pipeline for Detecting Fraudulent Financial Transactions.</strong>
</p>

---

## 📖 Overview

The **Bank Fraud Detection** project is a comprehensive Machine Learning solution designed to identify potentially fraudulent banking transactions in real-time. By leveraging advanced Feature Engineering and multiple classification architectures, this pipeline isolates anomalies based on user behavior, geographical data, and temporal logic.

This project covers the full AI lifecycle: from Exploratory Data Analysis (EDA) and K-Means Clustering to rigorous Hyperparameter Tuning, culminating in a serialized Production Pipeline ready for high-performance Web Integration.

## ✨ Key Features

1. **Intelligent Feature Engineering**: 
   - Extracts semantic time signatures (e.g., `TransactionHour`, `DayOfWeek`).
   - Calculates dynamic `TimeSinceLast` transaction (in seconds) to identify aggressive machine-speed fraud vectors.
2. **Unsupervised Clustering Analysis (K-Means + PCA)**:
   - Segments transactions into distinct behavioral profiles.
   - Evaluates cluster density using the *Elbow Method* and visualizes outputs smoothly in reduced 2D dimensions using Principal Component Analysis.
3. **Automated Model Arena (Auto-Selection)**:
   - Pitches top-tier algorithms against each other including **Decision Tree**, **Random Forest Classifier**, and **Gradient Boosting Classifier**.
   - Validates stability using 5-Fold Stratified Cross-Validation.
4. **Hyperparameter Tuning (`RandomizedSearchCV`)**:
   - Systematically tunes `max_depth`, `n_estimators`, `learning_rate`, etc., to squeeze out maximum accuracy without overfitting.
5. **Serialized Production Pipeline**:
   - A singular `fraud_detection_pipeline.pkl` artifact encapsulates the optimal `StandardScaler` standardisation and the Best Estimator for 1-line predictions.

## 📊 Performance & Metrics

After rigorous Cross-Validation and Hyperparameter testing against our banking dataset, the algorithm capabilities proved highly robust:

- **Best Model Found**: `Gradient Boosting Classifier`
- **Optimal Hyperparameters**: `{'n_estimators': 200, 'min_samples_split': 10, 'max_depth': 20, 'learning_rate': 0.1}`
- **Highest Accuracy Score (5-Fold CV)**: ⭐ **95.87%**

## 📂 Project Structure

```text
ML_Deteksipenipuanbank/
│
├── ml_project.ipynb              # The Core Machine Learning AI Notebook (EDA > Training > Tuning)
├── fraud_detection_pipeline.pkl  # Production-ready scikit-learn Pipeline (Scaler + Tuned Final Model)
├── decision_tree_model.h5        # Baseline Decision Tree model
├── model_clustering              # Baseline KMeans segmentation model
└── README.md                     # Project documentation
```

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3 installed along with Jupyter Notebook or VS Code Jupyter extensions.
Required libraries:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn yellowbrick
```

### Running the Notebook

1. Clone or download this repository.
2. Open `ml_project.ipynb` in your preferred Jupyter environment.
3. Select **Restart & Run All** to execute the pipeline from start to finish.
4. Watch as the code ingests the Kaggle dataset, generates new temporal features, visualizes PCA clusters, compares models, and outputs your custom `fraud_detection_pipeline.pkl`.


---
<i>This project serves as a cornerstone for advanced portfolio machine learning tasks, showcasing full-stack AI logic from raw Data to Pipeline Serialization.</i>
