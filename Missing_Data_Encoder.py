import pandas as pd
import numpy as np 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder  #labelencoder is depriciated
from sklearn.compose import ColumnTransformer  #new

data = pd.read_csv("Data copy.csv")

X = data.iloc[:,:-1].values
y = data.iloc[:,3].values


# print("X",X)
labelencoder_X = LabelEncoder()
# X[:,0] = labelencoder_X.fit_transform(X[:,0])
# onehot = OneHotEncoder(categorical_features= [0])             depriciated part
# X = onehot.fit_transform(X).toarray()

columnT = ColumnTransformer([('encoder',OneHotEncoder(),[0])], remainder='passthrough')
X = np.array(columnT.fit_transform(X), dtype=np.str)


print("X",X,type(X))