# -*- coding: utf-8 -*-
"""Prediction using Supervised ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WHgHVolv8GnNofGfVpmzvWDWtu00YQKI

# Importing the librairies
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

"""# Loading the dataset"""

from google.colab import drive
drive.mount('/content/drive')

score = pd.read_csv('/content/drive/MyDrive/student_scores.csv')

score.head()

score.describe()

"""# Visualizing the data"""

score.plot(x ='Hours', y='Scores', kind = 'bar')
plt.title('Student score according to the number of hours studied')  
plt.xlabel('Hours Studied')  
plt.ylabel('Score')  
plt.show()

score.plot(x ='Hours', y='Scores', kind = 'scatter')
plt.title('Student score according to the number of hours studied')  
plt.xlabel('Hours Studied')  
plt.ylabel('Score')  
plt.show()

"""# Train-Test-Split"""

y= score.Scores
X= score.drop(['Scores'] ,axis=1 )

X_train ,X_test ,y_train , y_test = train_test_split(X, y ,train_size=0.8 , test_size = 0.2)

"""# Training the model 
I choose to use Random Forest since it has much better predictive accuracy than a single decision tree and it works with default parameters
"""

forest_model =RandomForestRegressor(random_state=1)

forest_model.fit(X_train,y_train)

pred = forest_model.predict(X_test)

"""# Using differents metrics """

print("Mean absolute error : ")
print(mean_absolute_error(y_test, pred))

print("Mean absolute error : ")
print(mean_squared_error(y_test, pred, squared=False))

"""# Testing the model obtained"""

prediction = forest_model.predict(X_test)

df = pd.DataFrame({'Actual': y_test, 'Predicted': prediction})

df

dff = pd.DataFrame({'hours': 9.25},index=(0,1))  
hours=[20,9.25]
p =forest_model.predict(dff)[0]

print("for 9.25 hours studied the student may likely achieve ", p)