import pandas as pd 
from sklearn.preprocessing import StandardScaler, OneHotEncoder 
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer  #new
import numpy as np 


data = pd.read_csv("Data copy.csv")

X = data.iloc[:,:-1].values
y = data.iloc[:,3]

columnT = ColumnTransformer([('encoder',OneHotEncoder(),[0])], remainder='passthrough')
X = np.array(columnT.fit_transform(X), dtype=np.str)

X_train, y_train, X_test, y_test = train_test_split(X, y, random_state=1, train_size=0.7 )

print("X_train before", X_train)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

print("After", X_train)