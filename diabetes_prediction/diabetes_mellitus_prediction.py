# -*- coding: utf-8 -*-
"""diabetes_mellitus_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11pjYqI6wwnFblh9_gVTLuNOTATF6H5go

Import Dependedncies
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data colleaction and analysis"""

# load csv file to create dataframe
diabetes_data = pd.read_csv('/content/diabetes.csv')

#print first 5 rows of dataframe
diabetes_data.head()

# Give the shape of the dataframe
diabetes_data.shape

# Get standard mesurements
diabetes_data.describe()

#Value counts
diabetes_data['diabetes'].value_counts()

"""From this dataset, 8500 people are diabetic and 91500 people are not"""

diabetes_data['gender'].value_counts()

"""There are 58552 women and 41430 men"""

group_by_gender = diabetes_data.groupby('gender')

females = group_by_gender.get_group('Female')
males = group_by_gender.get_group('Male')

# Diabetic scores on Females
print('Females: ',females['diabetes'].value_counts())

# Diabetic sscores on Males
print('Males: ', males['diabetes'].value_counts())

"""4461 out of 58552 women are diabetic

4093 out of 41430 men are diabetic

Drop rows where Smoking History == 'No Info'
"""

diabetes_data = diabetes_data[diabetes_data['smoking_history'] != 'No Info']

"""Drop rows where Gender == 'Other'"""

diabetes_data = diabetes_data[diabetes_data['gender'] != 'Other']

"""Display Head"""

diabetes_data.head()

"""Encode Non numeric data
---

Gender
---

Female: 0

Male: 1




Smoking History
---

Never smoked: 0

Current smoker: 1

Former smoker: 2

Has ever smoked before: 3

Not currently smoking: 4
"""

#Gender
diabetes_data['gender'] = diabetes_data['gender'].replace({'Female': 0, 'Male': 1})

#Smoking History
diabetes_data['smoking_history'] = diabetes_data['smoking_history'].replace({'never': 0, 'current': 1, 'former': 2, 'ever': 3, 'not current': 4})

print(diabetes_data)

"""Get Mean value of each column after grouping by diabetes column"""

diabetes_data.groupby('diabetes').mean()

"""The average diabetic in this data is 60 years of age with a higher HbA1c level, glucose level and hypertension level"""

A = diabetes_data.drop(columns=['diabetes'], axis=1)
B = diabetes_data['diabetes']

print(A)
print(B)

"""Data Preprocessing"""

#Data standardization
scaler = StandardScaler()

#Fit calculates the mean and standard deviation and transform uses that data to
# help keep values between 0 and 1
A = scaler.fit_transform(A)

print(A)

"""Train Test Splitting"""

a_train, a_test, b_train, b_test = train_test_split(A, B, test_size=0.2, stratify=B, random_state=2)
print(A.shape, a_train.shape, a_test.shape)

"""Train the model"""

#Instantate the classifier
model = svm.SVC(kernel='linear')

#Train the model
model.fit(a_train, b_train)

"""Model Evaluation: Testing model accuracy"""

#Check accuracy of training data
a_train_prediction = model.predict(a_train)
training_data_accuracy = accuracy_score(a_train_prediction, b_train)

print('Accuracy score of the training data: ', training_data_accuracy)

#Check accuracy score of the testing data
a_test_prediction = model.predict(a_test)
testing_data_accuracy = accuracy_score(a_test_prediction, b_test)

print('Accuracy score of the testing data: ', testing_data_accuracy)

"""Predictive system using trained model"""

#This patient is diabetic. This cell checks the model's accuracy
input = (1,69.0,0,1,0,29.34,8.2,155)

#As numpy array
input_np = np.asarray(input)

#Reshape array to get prediction for just one instance
input_np_reshaped = input_np.reshape(1, -1)

#Standardize input data
std_data = scaler.transform(input_np_reshaped)
print(std_data)

prediction = model.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

"""Packaging the model with pickle"""

import pickle

with open('/content/diabetes_prediction_model.pkl', 'wb') as f:
  pickle.dump(model, f)