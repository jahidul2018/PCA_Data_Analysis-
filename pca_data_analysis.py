# -*- coding: utf-8 -*-
"""pca-data-analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nyIOeGEYTh7Xpia28igOAZ43hExYDD3h
"""

# importing package
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from numpy.linalg import eig

# defining a simple data 
marks = np.array([[3,4], [2,8], [6,9]])
print(marks)

# make a data frame
marks_fm = pd.DataFrame(marks,columns=['Bangla','english'])
marks_fm

plt.scatter(marks_fm['Bangla'],marks_fm['english'])

meanbycolumn = np.mean(marks.T, axis=1) 
print(meanbycolumn) 
ScaledData = marks - meanbycolumn

marks.T

ScaledData

# find the covaricene matrix of the scaled data
covmat = np.cov(ScaledData.T)
covmat

# find the corresponding eigen value and eigen vector of abvoe covariance matrix
eval, evec =eig(covmat)
print(eval)
print(evec)

# get original data projected to principal componeents as new axis
projectedData = evec.T.dot(ScaledData.T)
print(projectedData)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit_transform(marks)

# variance explanation ratio by each PC
pca.explained_variance_ratio_

# DataFrame for pca
pcdf = pd.DataFrame(data =pca.fit_transform(marks), columns=['pc1','pc2'])
pcdf

plt.scatter(pcdf['pc1'], pcdf['pc2'])

# how much weight each variable has in principal components
loadingWeight = pd.DataFrame(pca.components_.T, columns=['pc1','pc2'], index=['bangla', 'english'])
loadingWeight

# inverse transform
pca.inverse_transform(pca.fit_transform(marks))