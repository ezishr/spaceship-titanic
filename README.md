# SpaceShip Titanic - Machine Learning Predictions
## Objective
This project aims to predict the destination of passengers aboard a fictional spaceship based on various features, including their home planet, age, and other personal characteristics. By analyzing the relationships between these variables, we aim to build a robust machine-learning model that accurately forecasts passenger destinations. This project also seeks to uncover insights into passenger demographics and behaviors that influence their likelihood of being transported to specific destinations, with a focus on improving feature engineering and model performance.

## Project Workflow
The project follows the same approach as used in all ML projects. We will go through data collection, exploratory data analysis (EDA), feature engineering and extraction, preprocessing data, data cleansing, data training, and finally deployment of trained model.
* Data Collection
* Exploratory Data Analysis
* Feature Engineering and Extraction
* Preprocessing Data
* Data Cleansing
* Model Training
* Deployment

This README file will include sections data collection and model training. Other sections will be presented and discussed further in specific files mentioned in ***To Run (locally)*** section below.

## Data Collection
The only source of data is from the Kaggle competition about the same topic, which can be viewed [here.](https://www.kaggle.com/competitions/spaceship-titanic/discussion/309323)
There are two csv datasets which are `train.csv` for training purpose and `test.csv` for deployment purpose. The target column is `Transported` which determines if a passenger was transported to destination (True) or not (False). The `train.csv` has flaws in data so we will perform above mentioned workflows to make it ready for training. 

Since the `train.csv` dataset shows that every passenger has about 20% of missing values, we decided not to drop any passenger but rather tried to fill in the missing values based on existing relationships and relevant methods.

Further dataset description can be read [here.](https://www.kaggle.com/competitions/spaceship-titanic/data)

## Model Training
The target column that we are trying to predict is a `binary classification` problem. The problem is under supervised machine learning. After feature enginnering and extraction, we use multiple ML models using `train.csv` dataset and choose the model which gives us best accuracy.

The machine learning models considered to train the dataset in this project are :
- Decision Tree
- Random Forest
- XG Boosting
- Logistic Regression

## Libraries and Tools
- **NumPy** (v1.26.4): Used for numerical operations and array handling.
- **Pandas** (v2.2.2): Used for data manipulation and analysis.
- **Scikit-learn** (v1.3.0): Provides machine learning algorithms and evaluation metrics.
    + Metrics: accuracy_score, mean_absolute_error
    + Preprocessing: StandardScaler, LabelEncoder, OneHotEncoder
    + Model selection: cross_val_score,train_test_split
- **Matplotlib** (v3.9.1) and **Seaborn** (v0.13.2): Used for plotting and visualizations.

## To Run (locally)
Follow these steps to set up and run the project on your local machine:

#### Prerequisites

Ensure you have the following installed on your system:

- **Python: [Download here](https://www.python.org/downloads/)
- **Git**: [Download here](https://git-scm.com/downloads)
- **Virtual Environment**: Optional, but recommended for managing dependencies

#### Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/ezishr/spaceship-titanic.git
2. **Change to `eirlys` branch**:
   ```sh
   git checkout eirlys
4. **Install all the required dependencies inside a virtual environment**
   ```sh
   pip install -r requirements.txt
5. 

