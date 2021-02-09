#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import sklearn.preprocessing
from sklearn.linear_model import LinearRegression

#  linearr regression for each genre
def linreg(data, genre):
    y = data['katz'].values
    x = data.iloc[:, 4:17].values
    #
    x_scale = sklearn.preprocessing.scale(x)
    linreg = LinearRegression()
    model = linreg.fit(x_scale, y)
    f.write(genre)
    for j in range(len(model.coef_)):
        f.write(",%f" % model.coef_[j])
    f.write("\n")

f = open('linreg.csv', 'a+')
data0 = pd.read_csv('data_by_artist.csv')
for i in data0['genre'].unique():
    data1 = data0[data0['genre'] == i]
    linreg(data1, i)
f.close()
