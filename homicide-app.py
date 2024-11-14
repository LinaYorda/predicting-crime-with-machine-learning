import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os


st.sidebar.title('Menu')
page = st.sidebar.radio("Go to", ['Home', 'Data'])
st.sidebar.write("### About this project")
st.sidebar.write("""
This project aims to explore the applicability of various machine learning models to predict whether a crime was solved, based on a comprehensive dataset. Through exploratory data analysis (EDA) and the implementation of multiple predictive models, the study seeks to enhance the understanding of factors influencing crime resolution. The dataset used for this project is derived from the Murder Accountability Project, an extensively compiled database of homicides in the United States. It was downloaded from [Kaggle](https://www.kaggle.com/datasets/jyzaguirre/us-homicide-reports), and consists of more than 600k cases for the period between 1980 and 2014.
""")

if page == 'Home':
    st.title('Homicide Data Exploration for the period 1980-2014 in the USA')
    st.write("Four machine learning algorithms will be tested to predict whether a crime will be solved: Logistic Regression, Decision Tree, Random Forest and XGBoost. Each model will be evaluated based on accuracy and ROC curve performance to assess how effectively it distinguishes between solved and unsolved crimes. Additionally, important features contributing to the prediction will be identified and analyzed.")
 # Set a fixed width
    important_features = {
        "Important Feature Logistic Regression": "plots/features_logistric_reg.png",
        "Important Features Random Forest": "plots/important_features_random_forest.png",
        "Important Features Decision Tree": "plots/important_freature_decision_tree.png", 
        "Important Features XGBoost": "plots/important_features_xgboost.png"
    }

    confusion_matrix = {
        "Confusion Matrix Logistic Regression": "plots/confusion_matrix_log_regression.png",
        "Confusion Matrix Decision Tree": "plots/confusion_matrix_decision_tree.png",
        "Confusion Matrix Random Forest": "plots/consufion_matrix_random_forest.png", 
     "Confusion Matrix XGBoost": "plots/confusion_matrix_xgboost.png"
    }


    roc_curve = {
        "ROC Logistic Regression": "plots/ROC_regression.png",
        "ROC Decision Tree": "plots/ROC_decision_tree.png",
        "ROC Random Forerst": "plots/ROC_random_forest.png", 
        "ROC XGBoost": "plots/ROC_xgboost.png"
    }

    st.header("Important Features")
    col1, col2= st.columns(2)
    with col1:
        st.image(important_features["Important Feature Logistic Regression"], caption="Important Features Logistic Regression")
        st.image(important_features["Important Features Decision Tree"], caption="Important Features Decision Tree")
    with col2:
        st.image(important_features["Important Features Random Forest"], caption="Important Features Random Forest")
        st.image(important_features["Important Features XGBoost"], caption="Important Features XGBoost")

    st.header("Confusion Matrix")
    col1, col2= st.columns(2)
    with col1:
        st.image(confusion_matrix["Confusion Matrix Logistic Regression"], caption="Confusion Matrix Logistic Regression")
        st.image(confusion_matrix["Confusion Matrix Decision Tree"], caption="Confusion Matrix Decision Tree")
    with col2:
        st.image(confusion_matrix["Confusion Matrix Random Forest"], caption="Confusion Matrix Random Forest")
        st.image(confusion_matrix["Confusion Matrix XGBoost"], caption="Confusion Matrix XGBoost")



    st.header("ROC Curve")
    col1, col2= st.columns(2)
    with col1:
        st.image(roc_curve["ROC Logistic Regression"], caption="ROC Logistic Regression")
        st.image(roc_curve["ROC Decision Tree"], caption="ROC Decision Tree")
    with col2:
        st.image(roc_curve["ROC Random Forerst"], caption="ROC Random Forest")
        st.image(roc_curve["ROC XGBoost"], caption="ROC XGBoost")
else:
    st.title('Data Exploration')
    st.write("")
    cwd = os.getcwd()
    #print("Current working directory:", cwd)

# Define the relative path to the file
    file_path = os.path.join(cwd, 'data', 'database.csv')
    data = pd.read_csv('data/database.csv')
    st.write(data)
    st.write("The data has {} rows and {} columns.".format(data.shape[0], data.shape[1]))
    st.write("* The columns are: {}".format(data.columns.tolist()),)
    st.write("* The data types are: {}".format(data.dtypes))
    st.write("* The data has {} missing values.".format(data.isnull().sum().sum()))
    st.write("* The data has {} duplicate rows.".format(data.duplicated().sum()))
    st.header("Spearman Correlation")
    st.write("Strong Correlation with Perpetrator Age: A Spearman correlation test yielded a coefficient of 0.74, indicating a strong positive correlation between 'Perpetrator Age' and the likelihood of a crime being solved ('Crime Solved'). This suggests that older perpetrators are more likely to be involved in cases that are solved.")
    st.image("plots/spearman_corr.png", caption="Spearman Correlation")
    st.header("Chi-Square Analysis")
    st.write("Perpetrator Sex exhibits the strongest connections with both 'Crime Solved' and 'Perpetrator Race', indicating the critical role of the perpetrator’s sex in the crime-solving process. Interpersonal Relationships shows significant associations were observed between 'Victim Sex' and 'Perpetrator Sex/Race', and 'Perpetrator Sex' and 'Relationship', emphasizing the impact of gender and relationship dynamics.Crime Type Correlations: Notable but less intense associations with 'Relationship' and 'Weapon', suggesting how different aspects of a crime interlink with crime types.")
    st.image("plots/heatmap_Chi_square.png", caption="Chi-Square Analysis")
    st.write("-----------------------------------------------------------------------------------------------------------------")
    st.write("The full code, notebooks and images can be found on my [GitHub](https://github.com/LinaYorda/predicting-crime-with-machine-learning?tab=readme-ov-file).")





