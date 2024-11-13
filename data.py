import streamlit as st
import pandas as pd

st.title('Homicide Data Exploration')
st.write('The dataset was assembled and made publicly accessible by the Murder Accountability Project, an initiative led by Thomas Hargrove aimed at increasing transparency around homicide rates and justice efficacy in the United States. The project underscores the importance of open data in addressing social issues and enhancing accountability in criminal justice.')

def load_data():
    data = pd.read_csv('data/database.csv')
    return sample_data

sample_data = load_data()