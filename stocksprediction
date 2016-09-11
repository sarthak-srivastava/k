import pandas as pd
import quandl,math
import numpy as np
from sklearn import preprocessing,cross_validation,svm
from sklearn.linear_model import LinearRegression
df=quandl.get('WIKI/GOOGL')
print (df.head())
df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT']=(df['Adj. High']-df['Adj. Low'])/df['Adj. Low']*100.0
df['PCT_CG']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Close']*100.0
df = df[['Adj. Close', 'HL_PCT', 'PCT_CG', 'Adj. Volume']]
print(df.head())
forecast_col='Adj. Close'
df.fillna(-99999,inplace=True)
forecast_out=int(math.ceil(.001*len(df)))
df['label']=df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.head())
X=np.array(df.drop(['label'],1))
y=np.array(df['label'])
X=preprocessing.scale(X)
X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.4)
clf=LinearRegression()
clf.fit(X_train,y_train)
accuracy=clf.score(X_test,y_test)
print(accuracy)
