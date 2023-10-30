# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 22:52:03 2021

@author: muham
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import r2_score

veriler=pd.read_csv('maaslaryeni.csv')

x=veriler.iloc[:,2:5].values
y=veriler.iloc[:,5:].values
#print(veriler.corr()):matris oluşturur, değişkenler arasındaki bağlantıyı gösterir.

#lineer regresyon
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x,y)


model=sm.OLS(lin_reg.predict(x),x)
print(model.fit().summary())

print('Linear R2 degeri')
print(r2_score(y, lin_reg.predict(x)))


#polinomal regresyon
from  sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=4)
x_poly=poly_reg.fit_transform(x)

lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y)

print('poly OLS')
model2=sm.OLS(lin_reg2.predict(poly_reg.fit_transform(x)),x)
print(model2.fit().summary())

print('Polynomial R2 degeri')
print(r2_score(y, lin_reg2.predict(poly_reg.fit_transform(x))))

#çoklu doğrusal regresyon
from sklearn.preprocessing import StandardScaler

sc1=StandardScaler()
x_olcekli = sc1.fit_transform(x)
sc2=StandardScaler()
y_olcekli = np.ravel(sc2.fit_transform(y.reshape(-1,1)))


from sklearn.svm import SVR

svr_reg = SVR(kernel='rbf')
svr_reg.fit(x_olcekli,y_olcekli)


print('SVR OLS')
model3=sm.OLS(svr_reg.predict(x_olcekli),x_olcekli)
print(model3.fit().summary())


print('SVR R2 degeri')
print(r2_score(y_olcekli, svr_reg.predict(x_olcekli)))

#karar ağacı regresyonu
from sklearn.tree import DecisionTreeRegressor
r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(x,y)


print('Decision Tree OLS')
model4=sm.OLS(r_dt.predict(x),x)
print(model4.fit().summary())

print('Decision Tree R2 degeri')
print(r2_score(y, r_dt.predict(x)))

#Rassal Orman Regresyonu
from sklearn.ensemble import RandomForestRegressor
rf_reg=RandomForestRegressor(n_estimators = 10,random_state=0)
rf_reg.fit(x,y.ravel())


print('Random Forest OLS')
model5=sm.OLS(rf_reg.predict(x),x)
print(model5.fit().summary())

print('Random Forest R2 degeri')
print(r2_score(y, rf_reg.predict(x)))


#Ozet R2 değerleri
print('-----------------------')
print('Linear R2 degeri')
print(r2_score(y, lin_reg.predict(x)))

print('Polynomial R2 degeri')
print(r2_score(y, lin_reg2.predict(poly_reg.fit_transform(x))))

print('SVR R2 degeri')
print(r2_score(y_olcekli, svr_reg.predict(x_olcekli)))


print('Decision Tree R2 degeri')
print(r2_score(y, r_dt.predict(x)))

print('Random Forest R2 degeri')
print(r2_score(y, rf_reg.predict(x)))

