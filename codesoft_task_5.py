# -*- coding: utf-8 -*-
"""Codesoft_Task_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13xN3goXXbivMGe36USNxcvKBZLDnqRyp
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
from sklearn.linear_model import LogisticRegression

from google.colab import drive
drive.mount('/content/drive')

data=pd.read_csv("/content/drive/MyDrive/Colab Notebooks/DATA_SET/creditcard.csv")

data.info()

data.isnull().sum()

data.describe()

data.head()

data.shape

for col in data.columns:
  print(col)

data['Class'].value_counts()

print((data.groupby('Class')['Class'].count()/data['Class'].count())*100)
((data.groupby('Class')['Class'].count()/data['Class'].count())*100).plot.pie()

classes = data['Class'].value_counts()
normal_value = round(classes[0]/data['Class'].count()*100,2)
fraud_values = round(classes[1]/data['Class'].count()*100,2)
print(normal_value)
print(fraud_values)

data.corr()

plt.figure(figsize=(27,19))
sns.heatmap(corr, cmap = 'spring', annot= True )
plt.show()

legit = data[data.Class == 0]

fraud = data[data.Class==1]

legit.Amount.describe()

fraud.Amount.describe()

data.groupby('Class').describe()

data.groupby('Class').mean()

normal_sample = legit.sample(n=492)

new_dataset = pd.concat([normal_sample, fraud], axis = 0)

new_dataset

new_dataset['Class'].value_counts()

new_dataset.groupby('Class').mean()

delta_time = pd.to_timedelta(new_dataset['Time'], unit = 's')
new_dataset['time_hour']=(delta_time.dt.components.hours).astype(int)
new_dataset.drop(columns='Time', axis=1, inplace = True)

new_dataset

x = new_dataset.drop('Class', axis=1)

y = new_dataset['Class']

x.shape

y.shape

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.25, random_state = 3, stratify = y)

cols = list(x.columns.values)

normal_entries = new_dataset.Class==0
fraud_entries = new_dataset.Class==1

plt.figure(figsize=(20,70))
for n, col in enumerate(cols):
    plt.subplot(10,3,n+1)
    sns.histplot(x[col][normal_entries], color='blue', kde = True, stat = 'density')
    sns.histplot(x[col][fraud_entries], color='red', kde = True, stat = 'density')
    plt.title(col, fontsize=17)
plt.show()

model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_train)
pred_test = model.predict(x_test)

from sklearn.metrics import confusion_matrix
def Plot_confusion_matrix(y_test, y_pred):
    cm = confusion_matrix(y_test,pred_test)
    plt.clf()
    plt.show()

acc_score= round(accuracy_score(y_pred, y_train)*100,2)

print('the accuracy score for training data of our model is :', acc_score)

y_pred = model.predict(x_test)
acc_score = round(accuracy_score(y_pred, y_test)*100,2)

print('the accuracy score of our model is :', acc_score)

from sklearn import metrics

score = round(model.score(x_test, y_test)*100,2)
print('score of our model is :', score)

class_report = classification_report(y_pred, y_test)
print('classification report of our model: ', class_report)