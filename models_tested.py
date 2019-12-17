# preliminaries

import sys
assert sys.version_info >= (3, 5)

# Scikit-Learn ≥0.20 is required
import sklearn
assert sklearn.__version__ >= "0.20"

# Common imports
import numpy as np
import os

# To plot pretty figures
%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


# import data as pandas dataframe and preview it
pdata = pd.read_csv('toy_dataset_combined-withTimestamp.valsOnly.csv')
pdata.head()

# split data into training and testing
from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(pdata, test_size=0.2, random_state=42)

test_set.head()


# create X and Y values
# this is opposite of fast but I was tired and frustrated at this point
# note that to use the convenient to_numpy() method below, you MUST HAVE pandas version 0.25
X_train = train_set.iloc[:, [0,1,2,3,4,5,6,7]]
X_test = test_set.iloc[:, [0,1,2,3,4,5,6,7]]
Y_train = train_set.iloc[:, [8]]
Y_test = test_set.iloc[:, [8]]
y_train_ = Y_train.to_numpy()
y_train = y_train_.flatten()


# standardize training values
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

num_pipeline = Pipeline([('std_scaler', MinMaxScaler())])
pdata_x = num_pipeline.fit_transform(X_train)
pdata_y = y_train
pipeline.fit(pdata_x, pdata_y)

from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans

# simple test of KMeans using this data
pipeline = Pipeline([("kmeans", KMeans(n_clusters=30)), ("log_reg", LogisticRegression())])

# running GridSearch just for fun to see if my wild guess of n=50 clusters was a good one
from sklearn.model_selection import GridSearchCV
param_grid = dict(kmeans__n_clusters=range(2, 100))
grid_clf = GridSearchCV(pipeline, param_grid, cv=3, verbose=2)
grid_clf.fit(pdata_x, pdata_y)

# this output '4', oops.
grid_clf.best_params_
# {'kmeans__n_clusters': 4}

# trying DBSCAN
from sklearn.cluster import DBSCAN

# by chance, this dataset also followed the walkthrough in the book, 
# where widening the epsilon-neighborhood (eps) value from 0.05 to 0.2 dramatically improved the model 

dbscan = DBSCAN(eps=0.2, min_samples=5)
dbscan.fit(pdata_x)

# peek at the labels and indices
print(dbscan.labels_)
print(dbscan.core_sample_indices_)

# finally, tested Gaussian Mixture Model, which was straightforward, 
# but admittedly will take a bit of work to fully implement

from sklearn.mixture import GaussianMixture
gm = GaussianMixture(n_components=4, n_init=10)
gm.fit(pdata_x)

pipeline.fit(pdata_x, pdata_y)
