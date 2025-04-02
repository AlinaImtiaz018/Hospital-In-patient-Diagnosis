#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import seaborn as sns

def preprocessing_steps(filename):
    df1 = pd.read_csv("hospital_dataset.csv")

    df1.rename(columns={'ICD-10 (1-3-digit codes) main diagnosis': 'Codes',
                   'Diagnosis of hospital in-patients (main diagnosis)': 'Diagnosis',
                   'Patient\'s place of residence': 'Residence',
                   'under 1 year': 'Infants',
                   '1 to under 5 years': 'Infants',
                   '5 to under 10 years': '5 to 10',
                   '10 to under 15 years': '10 to 15',
                   '15 to under 18 years': '15 to 18',
                   '18 to under 20 years': '18 to 20',
                   '20 to under 25 years': '20 to 25',
                   '25 to under 30 years': '25 to 30',
                   '30 to under 35 years': '30 to 35',
                   '35 to under 40 years': '35 to 40',
                   ' 40 to under 45 years': '40 to 45',
                   '45 to under 50 years': '45 to 50',
                   '50 to under 55 years': '50 to 55',
                   '55 to under 60 years': '55 to 60',
                   '60 to under 65 years': '60 to 65',
                   '65 to under 70 years': '65 to 70',
                   '70 to under 75 years': '70 to 75',
                   '75 to under 80 years': '75 to 80',
                   '80 to under 85 years': '80 to 85',
                   '85 to under 90 years': '85 to 90'}, inplace=True)

    df1['1 to 18'] = df1[['Infants', '5 to 10', '10 to 15', '15 to 18']].mean(axis=1).round(1)
    df1['18 to 30'] = df1[['18 to 20', '20 to 25', '25 to 30']].mean(axis=1).round(1)
    df1['30 to 50'] = df1[['30 to 35', '35 to 40', '40 to 45', '45 to 50']].mean(axis=1).round(1)
    df1['50 to 70'] = df1[['50 to 55', '55 to 60', '60 to 65', '65 to 70']].mean(axis=1).round(1)
    df1['70 to 90'] = df1[['70 to 75', '75 to 80', '80 to 85','85 to 90']].mean(axis=1).round(1)

    dict = {
        'Certain infectious and parasitic diseases': 'Infections', 
                          'Malignant neoplasms': 'Malignant Neoplasms',
                          'Diseases of the blood and blood-forming organs etc': 'Blood',
                          'Diseases of the nervous system': 'Nervous System',
                          'Endocrine, nutritional and metabolic diseases': 'Metabolic',
                          'Diseases of the circulatory system': 'Circulatory',
                          'Diseases of the respiratory system': 'Respiratory',
                          'Diseases of the digestive system': 'Disgestive',
                          'Diseases of the musculoskeletal sys.a.conn.tissue': 'Musculoskeletal'
                }
    
    df1['Diagnosis'] = df1['Diagnosis'].replace(dict)

    df = df1[['Diagnosis', 'Residence', 'Year', 'Gender', '1 to 18', '18 to 30' ,'30 to 50','50 to 70','70 to 90']]

    return df


# In[ ]:




