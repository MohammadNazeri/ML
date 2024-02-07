# -*- coding: utf-8 -*-
"""Major Assignment 1-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MXcBtJXTeH3M6Qjt9J0onAZ8NQ4ZdOwT

#Question 2
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import classification_report

dataframe = pd.read_csv("/content/sample_data/lung cancer dataset.csv")

dataframe_num = dataframe
replacement_map = {'F': 1, 'M': 2}
dataframe_num['GENDER'] = dataframe_num['GENDER'].replace(replacement_map)
replacement_map = {'NO': 1, 'YES': 2}
dataframe_num['LUNG_CANCER'] = dataframe_num['LUNG_CANCER'].replace(replacement_map)
correlation_matrix = dataframe_num.corr()
#print(correlation_matrix)

df = dataframe_num
#df = dataframe_num.sample(100)
fig, ax = plt.subplots()

ax.bar('Lung cancer', df[(df['LUNG_CANCER'] == 2) & (df['ALLERGY '] == 1)].shape[0], width=0.1, label='No ALLERGY')
ax.bar('Lung cancer', df[(df['LUNG_CANCER'] == 2) & (df['ALLERGY '] == 2)].shape[0],width=0.1,label='ALLERGY')

ax.bar('No Lung cancer', df[(df['LUNG_CANCER'] == 1) & (df['ALLERGY '] == 1)].shape[0], width=0.1, label='No ALLERGY')
ax.bar('No Lung cancer', df[(df['LUNG_CANCER'] == 1) & (df['ALLERGY '] == 2)].shape[0],width=0.1,label='ALLERGY')

ax.bar('Lung cancer1', df[(df['LUNG_CANCER'] == 2) & (df['ALCOHOL CONSUMING'] == 1)].shape[0], width=0.1, label='No ALCOHOL CONSUMING')
ax.bar('Lung cancer1', df[(df['LUNG_CANCER'] == 2) & (df['ALCOHOL CONSUMING'] == 2)].shape[0],width=0.1,label='ALCOHOL CONSUMING')

ax.bar('No Lung cancer1', df[(df['LUNG_CANCER'] == 1) & (df['ALCOHOL CONSUMING'] == 1)].shape[0], width=0.1, label='No ALCOHOL CONSUMING')
ax.bar('No Lung cancer1', df[(df['LUNG_CANCER'] == 1) & (df['ALCOHOL CONSUMING'] == 2)].shape[0],width=0.1,label='ALCOHOL CONSUMING')

ax.set_title('Lung Cancer')
ax.legend()

dataframe_x = dataframe_num[dataframe_num.columns.difference(['LUNG_CANCER'])]
X_train, X_test, y_train, y_test = train_test_split(dataframe_x, dataframe_num['LUNG_CANCER'], test_size=0.3)

model = LogisticRegression(random_state=0,penalty='l2')
model.fit(X_train, y_train)
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)
report = classification_report(y_train, y_train_pred)
print("It is report classification on training data:  ",report)
report = classification_report(y_test, y_test_pred)
print("It is report classification on testing data:  ",report)