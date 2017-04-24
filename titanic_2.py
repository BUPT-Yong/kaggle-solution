# Load in our libraries
import pandas as pd
import numpy as np
import re
import sklearn
#import xgboost as xgb
import seaborn as sns
import matplotlib.pyplot as plt
# matplotlib inline

import plotly.offline as py
#py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls

# Going to use these 5 base models for the stacking
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, ExtraTreesClassifier
from sklearn.svm import SVC
from sklearn.cross_validation import KFold

# Load in the train and test datasets
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# Store our passenger ID for easy access
PassengerId = test['PassengerId']

#print (train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean())

#print (train[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean())

train = train.values
test = test.values

print type(train)

X = train[:,1:]
Y = train[:,0]

print X

print Y